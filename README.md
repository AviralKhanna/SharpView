Our project, **"SharpView: Advanced Low Light Image Enhancement Tool using C++,"** aims to solve the problem of enhancing images captured in low-light or degraded conditions. We wanted to create a lightweight, standalone tool that doesn’t rely on external libraries like OpenCV, making it efficient even on low-end devices.  

---

### **Objective**
The main goal was to build a robust image enhancement tool that improves image clarity and quality through techniques such as brightness adjustment, contrast enhancement, gamma correction, and Gaussian smoothing. We specifically focused on ensuring the tool could work efficiently on devices with limited resources, making it ideal for applications like mobile devices, embedded systems, or low-end computers.  

---

### **Key Features**
- **Lightweight Design**: The tool is optimized for devices with minimal hardware resources.  
- **Image Processing Techniques**: We implemented five core algorithms:
  1. **Gamma Correction**: To adjust brightness and tonal balance.  
  2. **Gaussian Smoothing**: To reduce noise without losing important details.  
  3. **Gray World Color Balance**: To make colors appear more natural by balancing RGB channels.  
  4. **Brightness Adjustment**: To make dark images more visible.  
  5. **Contrast Enhancement**: To bring out details in the light and dark areas.  
- **Multi-Format Support**: It works with common image formats like JPEG, PNG, BMP, and TIFF.  
- **Interactive User Interface**: We designed a user-friendly interface that allows real-time feedback and iterative enhancements, so users can adjust parameters like brightness and contrast on the fly.  

---

### **System Architecture**
The tool has three main components:  
1. **Frontend**: Built using HTML, CSS, and JavaScript, it allows users to upload images, preview enhancements, and download results.  
2. **Backend**: Powered by Flask, it manages user requests and communicates with the core processing engine.  
3. **Core Processing Engine**: Written in C++, this is where all the image enhancement algorithms are implemented.  

**How It Works**:  
- The user uploads an image through the web interface.  
- The backend sends the image to the C++ engine for processing.  
- The enhanced image is returned to the frontend, where the user can preview it, make further adjustments, or download it.  

---

### **Technical Specifications**
We implemented the core algorithms in C++ for high performance. The backend is built with Flask in Python, and the frontend uses vanilla JavaScript to ensure simplicity and responsiveness.  

The tool is lightweight, processing images within 3–5 seconds on low-end devices, and works efficiently even on systems with 2GB RAM. It supports iterative processing, where users can make adjustments in real-time for better results.  

---

### **Image Processing Pipeline**
1. **Input**: Users upload images, which are converted into a structured format (PPM) for processing.  
2. **Enhancement Techniques**: The tool applies a series of enhancements:  
   - Noise reduction with Gaussian filtering.  
   - Brightness and contrast adjustments.  
   - Gamma correction to improve tonal balance.  
   - Color balancing with the Gray World algorithm.  
3. **Output**: The final enhanced image is saved in formats like JPEG or PNG.  

---

### **Motivation and Use Cases**
I was inspired to work on this project because of its real-life applications. Low-light image enhancement is crucial for:  
- **General Users**: Improving personal photos.  
- **Professionals**: Assisting photographers and researchers.  
- **Security Applications**: Enhancing surveillance footage to improve visibility.  
- **Education**: Teaching core image processing techniques.  

Our tool is particularly useful for resource-constrained devices, bridging the gap between complex image processing systems and practical, efficient solutions.  

---

### **Core Algorithms**
We implemented the following algorithms from scratch:  
1. **Gamma Correction**: Adjusts brightness using a non-linear formula:  
   \[ I_{\text{output}} = I^\gamma_{\text{input}} \]  
   (Where \(\gamma < 1\) increases brightness, and \(\gamma > 1\) darkens it.)  
2. **Gaussian Smoothing**: Reduces noise with a weighted kernel while preserving edges.  
3. **Gray World Color Balance**: Balances RGB channels to neutralize unnatural color casts.  
4. **Brightness Adjustment**: Modifies pixel intensity based on user input.  
5. **Contrast Enhancement**: Increases the difference between light and dark regions for better detail visibility.  

---

### **Results**
The tool performs well, delivering enhanced images with improved brightness, reduced noise, and balanced colors. Real-time feedback allows users to customize enhancements to suit their needs. The before-and-after comparisons clearly show how the quality of low-light images is improved.  

---

### **Conclusion**
This project demonstrates how efficient and lightweight software design can address real-world challenges. By combining C++ for performance, Flask for flexibility, and an intuitive frontend, we created a scalable solution that works on low-end devices without sacrificing quality.  

This project not only solidified my understanding of image processing but also showed me how theoretical concepts can translate into impactful real-world applications.  

---
