# Galaxy Image Simplification using Generative AI

### Overview
This project presents a novel approach to simplifying galaxy images using Generative AI techniques. By transforming complex galaxy images into a simplified "skeletonized" form, the method enables more accurate quantitative analysis of galaxy shapes. The data used in this project is publicly available, including a catalog of simplified galaxy images derived from the DESI Legacy Survey.

### Features
- **Generative AI Application**: Utilizes Conditional Generative Adversarial Networks (cGANs) to convert complex galaxy images into simplified forms.
- **ResNet Architecture**: Implements a ResNet-based architecture for improved feature extraction and classification of galaxy images, enhancing the model's ability to distinguish between different galaxy types.
- **Post-Processing GAN**: Employs a second cGAN for post-processing to smooth and connect broken lines in the generated images, ensuring higher fidelity in the final output.
- **Image Processing Techniques**: Applies advanced image processing methods, including skeletonization and dilation, to enhance the visibility of galaxy structures.
- **Data Availability**: Provides access to a comprehensive dataset of galaxy images and the corresponding simplified outputs for research and analysis.

## Getting Started

### Installation
1. Create a Virtual Environment:
    ```bash
    python -m venv venv
    ```

2. Activate the Virtual Environment:
    - On Windows:
    ```
    venv\Scripts\activate
    ```
    - On macOS/Linux:
    ```
    source venv/bin/activate
    ```

3. Clone the repository:
   ```bash
   git clone https://github.com/SaiTeja-Erukude/galaxy-image-simplification-using-genai.git
   cd galaxy-image-simplification
   ```

4. Install the Required Packages:
    ```
    pip install -r requirements.txt
    ```