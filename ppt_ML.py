from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# Create a presentation
prs = Presentation()

# Layouts
title_slide_layout = prs.slide_layouts[0]
bullet_slide_layout = prs.slide_layouts[1]

# Title Slide
slide = prs.slides.add_slide(title_slide_layout)
slide.shapes.title.text = "PRNU-Based Device Identification using Machine Learning"
slide.placeholders[1].text = "Presented by:\nMariya Bashir  & Zakir Hussain Lone \nMCA Students, 2025"

# Helper function for bullet slides
def add_bullet_slide(title, bullets):
    slide = prs.slides.add_slide(bullet_slide_layout)
    slide.shapes.title.text = title
    content = slide.placeholders[1]
    tf = content.text_frame
    tf.clear()
    for bullet in bullets:
        p = tf.add_paragraph()
        p.text = bullet
        p.level = 0
        p.font.size = Pt(18)
        p.font.color.rgb = RGBColor(40, 40, 40)
        p.alignment = PP_ALIGN.LEFT

# Slides
add_bullet_slide("Objective", [
    "Identify which smartphone captured an image using ML.",
    "Use PRNU features and device metadata for classification."
])

add_bullet_slide("Data Collection", [
    "500 images captured per student using their mobile phones.",
    "Images converted to .jpg/.png format and resized to 256×256."
])

add_bullet_slide("Feature Extraction", [
    "Extracted GLCM features: mean, std dev, energy, correlation, entropy.",
    "Added manual features: Manufacturer, Model, Unit_ID."
])

add_bullet_slide("Dataset Preparation", [
    "Saved features into CSV file per student.",
    "Collected all CSVs and merged into one master dataset."
])

add_bullet_slide("Preprocessing", [
    "Performed normalization on all numerical features.",
    "Applied train-test split (e.g., 80/20) for evaluation."
])

add_bullet_slide("Algorithms Used", [
    "K-Nearest Neighbors (KNN)",
    "Decision Tree",
    "Random Forest",
    "Logistic Regression"
])

add_bullet_slide("Model Evaluation", [
    "Compared accuracy across all algorithms.",
    "Random Forest and KNN performed best on test data.",
    "Accuracy depends on feature quality and phone diversity."
])

add_bullet_slide("Conclusion", [
    "ML algorithms can classify images using PRNU features.",
    "Manual + GLCM features gave decent accuracy.",
    "Future scope: explore CNN or deeper feature extraction."
])

add_bullet_slide("Thank You", [
    "Presented by:",
    "Zakir Hussain Lone & Mariya Bashir",
    "MCA – 2025"
])

# Save the presentation
prs.save("PRNU_Device_Identification_ML_Final_Presentation.pptx")
print("✅ Presentation saved as 'PRNU_Device_Identification_ML_Final_Presentation.pptx'")
