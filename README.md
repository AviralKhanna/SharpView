**"SharpView: Advance Low Light Image Enhancement Tool using C++"**, is a comprehensive solution aimed at improving the visual quality of low-light and degraded images. Here's a detailed explanation to help you explain it to your professor:

---

### **1. Project Objective**
The primary goal is to develop a standalone, lightweight image enhancement tool in C++ that:
- Enhances image quality using techniques like brightness adjustment, contrast enhancement, gamma correction, and Gaussian smoothing.
- Operates efficiently on resource-constrained devices without relying on external libraries.

---

### **2. Key Features**
- **Lightweight Design**: Optimized for low-end devices.
- **Multi-Format Support**: Compatible with JPEG, PNG, BMP, and TIFF formats.
- **Core Algorithms**:
  - **Gamma Correction**: Adjusts brightness and tonal balance.
  - **Gaussian Smoothing**: Reduces noise while preserving edges.
  - **Gray World Color Balance**: Balances RGB channels for natural colors.
  - **Brightness & Contrast Adjustments**: Enhances visibility and detail clarity.
- **User Interactivity**: Allows real-time adjustments for iterative enhancements.

---

### **3. System Architecture**
The system is modular, comprising:
1. **Frontend (UI)**: Built with HTML, CSS, and JavaScript, allowing users to upload, preview, and download images.
2. **Backend (Flask)**: Manages requests, triggers C++ processes, and handles image processing.
3. **Core Image Processing (C++)**: Implements enhancement algorithms.

**Workflow**:
1. User uploads an image via the UI.
2. Backend sends the image to the C++ engine for processing.
3. Enhanced image is returned to the user for preview and further adjustments.

---

### **4. Technical Specifications**
- **Languages**: C++ (core algorithms), Python (backend), HTML/CSS/JS (frontend).
- **Hardware Requirements**:
  - Minimum: Dual-core processor, 2GB RAM.
  - Recommended: Quad-core processor, 4GB RAM, basic GPU.
- **Processing Speed**: Enhances images in 3-5 seconds on low-end devices.

---

### **5. Image Enhancement Pipeline**
1. **Input**: Accepts images in common formats and converts them to PPM for processing.
2. **Processing**:
   - Noise reduction via Gaussian filtering.
   - Brightness and contrast adjustments.
   - Gamma correction for tonal balance.
   - Gray-world algorithm for color balance.
3. **Output**: Enhanced image in desired formats (JPEG/PNG).

---

### **6. Use Cases**
- **General Users**: Enhance personal photos.
- **Professionals**: Photographers and researchers can use it for optimizing images.
- **Security**: Improves visibility in surveillance images.
- **Education**: Demonstrates core computer vision techniques.

---

### **7. Algorithms**
- **Gamma Correction**:
  - Formula: \( I_{\text{output}} = I^\gamma_{\text{input}} \)
  - Adjusts brightness with a non-linear transformation.
- **Gaussian Smoothing**:
  - Uses a Gaussian kernel to reduce noise while preserving details.
- **Gray World Algorithm**:
  - Balances RGB channels assuming the average scene color is gray.
- **Brightness Adjustment**:
  - Modifies pixel intensity linearly.
- **Contrast Enhancement**:
  - Formula: \( I' = I_{\text{avg}} + C \cdot (I - I_{\text{avg}}) \)
  - Boosts differences between light and dark regions.

---

### **8. Results**
- Enhanced images exhibit improved brightness, reduced noise, and balanced colors.
- Real-time feedback ensures user-controlled adjustments.
- Demonstrated efficiency on low-resource devices.

---

### **9. Conclusion**
The project successfully bridges academic concepts with real-world applications by creating a scalable, lightweight image enhancement tool. It is a versatile solution for users across various domains and a testament to efficient software design.

---
