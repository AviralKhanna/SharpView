const viewButton = document.getElementById("viewButton");
const enhanceButton = document.getElementById("enhanceButton");
const imageModal = document.getElementById("imageModal");
const modalImages = document.getElementById("modalImages");
const closeButton = document.querySelector(".close");

let originalImageURL = null;

// Show the uploaded image on clicking "View Image"
viewButton.addEventListener("click", () => {
    const imageFile = document.getElementById("imageUpload").files[0];
    if (!imageFile) {
        alert("Please upload an image first.");
        return;
    }
    originalImageURL = URL.createObjectURL(imageFile);
    modalImages.innerHTML = `<img src="${originalImageURL}" alt="Original Image">`;
    openModal();
});

// Enhance the image on clicking "Enhance Image"
enhanceButton.addEventListener("click", async () => {
    const imageFile = document.getElementById("imageUpload").files[0];
    if (!imageFile) {
        alert("Please upload an image first.");
        return;
    }

    const formData = new FormData();
    formData.append("image", imageFile);

    try {
        // Send the request to the Flask server
        const response = await fetch("http://localhost:5000/enhance", {  // Update to Flask server URL
            method: "POST",
            body: formData
        });

        // Log the response status for debugging
        console.log("Response status:", response.status);

        const data = await response.json();
        console.log("Response data:", data); // Log the response data for debugging

        if (data.success) {
            displayEnhancedImages(data.images);
        } else {
            alert("Image enhancement failed: " + data.message);
        }
    } catch (error) {
        console.error("Error:", error);
    }
});

function displayEnhancedImages(imagePaths) {
    modalImages.innerHTML = "";
    imagePaths.forEach((path) => {
        const img = document.createElement("img");
        // Use full URL path for Flask server images
        img.src = `http://localhost:5000${path}`;
        img.alt = "Enhanced Image";
        modalImages.appendChild(img);
    });
    openModal();
}

function openModal() {
    imageModal.style.display = "flex";
}

function closeModal() {
    imageModal.style.display = "none";
}

closeButton.addEventListener("click", closeModal);

window.addEventListener("click", (e) => {
    if (e.target === imageModal) {
        closeModal();
    }
});


// Function to fetch and display all images
async function fetchAllImages() {
    try {
        const response = await fetch("http://localhost:5000/images");
        const data = await response.json();

        if (data.success) {
            displayImages(data.images);
        } else {
            alert("Failed to retrieve images: " + data.message);
        }
    } catch (error) {
        console.error("Error fetching images:", error);
    }
}

function displayEnhancedImages(imagePaths) {
    modalImages.innerHTML = "";
    imagePaths.forEach((path) => {
        const img = document.createElement("img");
        // Use the server route to access images in the enhanced folder
        const filename = path.split('/').pop(); // Extract filename from path
        img.src = `http://localhost:5000/images/${filename}`;
        img.alt = "Enhanced Image";
        img.style.width = "100%";
        img.style.height = "auto";
        modalImages.appendChild(img);
    });
    openModal();
}

// Call fetchAllImages function when needed
// For example, you could call it on button click or when the page loads
document.getElementById("yourButtonId").addEventListener("click", fetchAllImages);
