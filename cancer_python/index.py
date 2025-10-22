import streamlit as st
import plotly.express as px
import pandas as pd

st.markdown(
    "<h1 style='text-align: center;'>Comparative Oncology Data Analysis</h1>", 
    unsafe_allow_html=True
)

from PIL import Image 
img = Image.open("cancer1.webp")
st.image(img, width=800)
st.subheader("About")
st.write("Cancer is a disease in which some of the body’s cells grow and multiply in an uncontrolled way. Unlike normal cells, which grow, divide, and die in an orderly manner, cancer cells keep dividing and can form a lump called a tumor (except in cancers of the blood, like leukemia). These abnormal cells can spread to other parts of the body through the blood or lymph system, a process known as metastasis. Cancer is not a single illness but a group of related diseases, and it can affect almost any organ or tissue in the body")
st.markdown(
    """
    <div style='background-color:#F0F8FF; padding:15px; border-radius:10px;'>
    <h4 style='color:#2C7BE5;'>🎯 Project Purpose</h4>
    <p style='color:#000000;'>
    The purpose of this project is to analyze and compare multiple types of cancers 
    across different age groups, genders, and stages. By studying survival rates, 
    cure percentages, and mortality trends, this analysis aims to uncover insights 
    that can support research, awareness, and healthcare decision-making.
    </p>
    </div>
    """,
    unsafe_allow_html=True
)

cancer_files = {
    "Esophageal Cancer": "2esophageal cancer.csv",
    "Pancreatic Cancer": "1pancreatic_cancer_dataset.csv",
    "Liver Cancer": "3liver_cancer.csv",
    "Lung Cancer": "4lung_cancer.csv",
    "Ovarian Cancer": "5ovarian cancer.csv",
    "Myeloma Cancer": "8myeloma Cancer.csv",
    "Stomache Cancer": "6stomache cancer.csv",
    "Laryngeal Cancer": "9Laryngeal Cancer.csv",
    "Brain Cancer": "7brain cancer.csv",
    "Acute myeloid leukemia": "10Acute_myeloid_leukemia.csv",
    "Bone Cancer" :"bone_cancer_data.csv",
    "Breast Cancer" :"breast_cancer_data.csv",
    "Skin Cancer" :"skin_cancer_data.csv",
    "Retinoblastoma Cancer" :"retinoblastoma_data.csv"
}


cancer_type = st.sidebar.selectbox("Select Cancer Type", list(cancer_files.keys()))
df = pd.read_csv(cancer_files[cancer_type])


df = df.rename(columns={
    "Survival_R": "Survival_Rate",
    "Death_Rat": "Death_Rate",
    "Cure%": "%Cure",
    "Cure_Rate": "%Cure"
})

st.subheader(f"{cancer_type}" )

# === Esophageal Cancer ===
if cancer_type == "Esophageal Cancer":

    st.text(
        "Esophageal cancer is a type of cancer that starts in the esophagus, the long tube that carries food and liquids from your throat to your stomach. "
        "In this cancer, the cells inside the lining of the esophagus grow in an uncontrolled way and form a tumor. "
        "This can make swallowing food or drinks difficult, cause chest pain, weight loss, or a long-lasting cough."
    )


    fig1 = px.bar(
        df, x="Age_Group", y="Survival_Rate", color="Gender",
        barmode="group", text_auto=True,
        title="📊 Esophageal Cancer - Survival Rate by Age Group"
    )
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.line(
        df, x="Age_Group", y="Death_Rate", color="Gender", markers=True,
        title="📈 Esophageal Cancer - Death Rate Trend"
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown( """ <h3 style='text-align:center; color:#00008B; font-family: Playfair Display;'> All You Need to Know About Esophageal Cancer </h3> """, unsafe_allow_html=True )

    
    with st.expander("Symptoms of Esophageal Cancer"):
        st.write("""
        • Difficulty swallowing (feeling like food is stuck)  
        • Unintentional weight loss  
        • Chest pain or burning sensation  
        • Persistent heartburn or acid reflux  
        • Hoarse voice or chronic cough  
        • Vomiting or regurgitation of food  
        • Feeling full quickly while eating  
        • Fatigue or weakness  
        """)
    with st.expander("Effects of Esophageal Cancer"):
        st.write("""
    • Difficulty swallowing food or liquids  
    • Chest pain or discomfort  
    • Unintentional weight loss  
    • Fatigue and weakness  
    • Chronic cough or hoarseness  
    • Malnutrition due to reduced intake  
    • Acid reflux or heartburn  
    • Increased risk of infections  
    """) 
    with st.expander("Causes of Esophageal Cancer"):
        st.write("""
    • Long-term gastroesophageal reflux disease (GERD)  
    • Smoking or tobacco use  
    • Excessive alcohol consumption  
    • Obesity or unhealthy diet  
    • Barrett’s esophagus (precancerous condition)  
    • Genetic predisposition / family history of cancer  
    • Exposure to certain chemicals or toxins  
    • Achalasia (a disorder affecting esophagus muscles)  
    """ )
    with st.expander("Treatments of Esophageal Cancer"):
        st.write("""
    • Surgery to remove the tumor or part of the esophagus  
    • Radiation therapy to kill cancer cells  
    • Chemotherapy to target and destroy cancer cells  
    • Targeted therapy for specific cancer cell types  
    • Immunotherapy to boost the body's immune response  
    • Palliative care to relieve symptoms and improve quality of life  
    • Lifestyle changes and nutritional support during treatment  
    """)
          












 

    



# === Pancreatic Cancer ===
if cancer_type == "Pancreatic Cancer":
    st.text("Pancreatic cancer is a type of cancer that starts in the pancreas, an organ behind the stomach that helps with digestion (by making enzymes) and controls blood sugar (by making insulin).In this cancer, cells in the pancreas grow uncontrollably and form a tumor. It often spreads quickly and is hard to detect early because symptoms usually appear late.")
    fig1 = px.area(df, x="Age_Group", y="%Cure", color="Gender",
                   title="📈 Pancreatic Cancer - Cure % Trend by Age Group")
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.bar(df, x="Stage_of_Cancer", y="Survival_Rate", color="Gender",
                  barmode="group", text_auto=True,
                  title="📊 Pancreatic Cancer - Survival Rate by Stage")
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown( """ <h3 style='text-align:center; color:#00008B; font-family: Playfair Display;'> All You Need to Know About Pancreatic Cancer </h3> """, unsafe_allow_html=True )
    with st.expander("Symptoms of Pancreatic Cancer"):
        st.write("""
    • Abdominal pain that radiates to the back  
    • Unexplained weight loss  
    • Loss of appetite  
    • Jaundice (yellowing of skin and eyes)  
    • Nausea and vomiting  
    • Fatigue and weakness  
    • New-onset diabetes  
    • Dark urine or pale stools  
    """)
    with st.expander("Effects of Pancreatic Cancer"):
        st.write("""
    • Difficulty digesting food  
    • Malnutrition due to poor nutrient absorption  
    • Weight loss and muscle wasting  
    • Fatigue and weakness  
    • Jaundice (yellowing of skin and eyes)  
    • Increased risk of diabetes or blood sugar issues  
    • Pain in abdomen and back  
    """)


    with st.expander("Causes of Pancreatic Cancer"):
        st.write("""
    • Smoking or tobacco use  
    • Obesity and sedentary lifestyle  
    • Chronic pancreatitis (inflammation of the pancreas)  
    • Family history of pancreatic cancer  
    • Genetic mutations (BRCA2, PALB2, etc.)  
    • Diabetes and insulin resistance  
    • Age (risk increases after 60)  
    """)


    with st.expander("Treatments of Pancreatic Cancer"):
        st.write("""
    • Surgery to remove the tumor or part of the pancreas  
    • Chemotherapy to kill cancer cells  
    • Radiation therapy  
    • Targeted therapy for specific cancer types  
    • Immunotherapy in certain cases  
    • Palliative care to relieve pain and improve quality of life  
    • Lifestyle changes and nutritional support  
    """)    


   

    



   



# === Liver Cancer ===
if cancer_type == "Liver Cancer":
    st.text("Liver cancer is a type of cancer that starts in the liver, the large organ in your upper right belly that helps clean the blood, digest food, and store energy.In this cancer, liver cells begin to grow abnormally and uncontrollably, forming a tumor. It can affect the liver’s ability to filter toxins, make proteins, and regulate body functions.")
    fig1 = px.pie(df, names="Stage_of_Cancer", values="Death_Rate",
                  title="Liver Cancer - Death Rate Distribution by Stage")
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.bar(df, x="Age_Group", y="Survival_Rate", color="Gender",
                  title="Liver Cancer - Survival Rate by Age Group")
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown( """ <h3 style='text-align:center; color:#00008B; font-family: Playfair Display;'> All You Need to Know About Liver Cancer </h3> """, unsafe_allow_html=True )
    with st.expander("Symptoms of Liver Cancer"):
        st.write("""
    • Unexplained weight loss  
    • Loss of appetite  
    • Upper abdominal pain or swelling  
    • Nausea and vomiting  
    • Fatigue and weakness  
    • Jaundice (yellowing of skin and eyes)  
    • Swelling in legs and ankles  
    • Dark-colored urine  
    """)


    with st.expander("Effects of Liver Cancer"):
        st.write("""
    • Impaired liver function  
    • Fatigue and weakness  
    • Malnutrition due to poor digestion  
    • Fluid accumulation in the abdomen (ascites)  
    • Jaundice and skin problems  
    • Increased risk of bleeding and bruising  
    • Weight loss and muscle wasting  
    """)


    with st.expander("Causes of Liver Cancer"):
        st.write("""
    • Chronic hepatitis B or C infection  
    • Cirrhosis (scarring of the liver)  
    • Heavy alcohol consumption  
    • Obesity and fatty liver disease  
    • Diabetes  
    • Family history of liver cancer  
    • Exposure to aflatoxins (from moldy food)  
    """)


    with st.expander("Treatments of Liver Cancer"):
        st.write("""
    • Surgery to remove part of the liver or liver transplant  
    • Ablation therapy (destroying tumor with heat or chemicals)  
    • Chemotherapy  
    • Radiation therapy  
    • Targeted therapy for specific cancer cells  
    • Immunotherapy to boost the immune system  
    • Palliative care for symptom relief  
    """)




 
# === Lung Cancer ===
if cancer_type == "Lung Cancer":
    st.text("Lung cancer is a type of cancer that starts in the lungs, the organs that help you breathe and supply oxygen to your body.In this cancer, cells in the lungs grow uncontrollably and form a tumor. It can block air passages, spread to other parts of the body, and make breathing difficult. Smoking is the main cause, but non-smokers can also get it")
    fig1 = px.violin(df, x="Stage_of_Cancer", y="Survival_Rate", color="Gender",
                     box=True, points="all",
                     title="🌫 Lung Cancer - Survival Rate Distribution by Stage")
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.histogram(df, x="Survival_Rate", color="Gender", nbins=10, barmode="overlay",
                        title="Lung Cancer - Survival Rate Histogram")
    st.plotly_chart(fig2, use_container_width=True) 
    st.markdown( """ <h3 style='text-align:center; color:#00008B; font-family: Playfair Display;'> All You Need to Know About Lung Cancer </h3> """, unsafe_allow_html=True )
    with st.expander("Symptoms of Lung Cancer"):
        st.write("""
    • Persistent cough that worsens over time  
    • Coughing up blood or rust-colored sputum  
    • Shortness of breath  
    • Chest pain or discomfort  
    • Hoarseness  
    • Unexplained weight loss  
    • Fatigue and weakness  
    • Frequent respiratory infections (bronchitis, pneumonia)  
    """)


    with st.expander("Effects of Lung Cancer"):
        st.write("""
    • Difficulty breathing and reduced oxygen levels  
    • Fatigue and weakness  
    • Chest pain  
    • Malnutrition and weight loss  
    • Fluid buildup around lungs (pleural effusion)  
    • Spread to other organs (metastasis)  
    """)


    with st.expander("Causes of Lung Cancer"):
        st.write("""
    • Smoking (tobacco use)  
    • Exposure to secondhand smoke  
    • Exposure to radon gas  
    • Exposure to asbestos or other carcinogens  
    • Air pollution  
    • Family history of lung cancer  
    • Genetic mutations  
    """)


    with st.expander("Treatments of Lung Cancer"):
        st.write("""
    • Surgery to remove part or all of the lung  
    • Radiation therapy  
    • Chemotherapy  
    • Targeted therapy for specific cancer cells  
    • Immunotherapy to boost the immune system  
    • Palliative care for symptom relief  
    """)

    




# === Ovarian Cancer ===
elif cancer_type == "Ovarian Cancer":
    st.text("Ovarian cancer is a type of cancer that starts in the ovaries, the female reproductive organs that produce eggs and hormones.In this cancer, the cells in the ovary grow uncontrollably and form a tumor. Since the ovaries are deep in the abdomen, symptoms often appear late, making it harder to detect early")
    fig1 = px.treemap(df, path=["Stage_of_Cancer", "Gender"], values="Death_Rate",
                      title="🌸 Ovarian Cancer - Death Rate by Stage & Gender")
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.bar(df, x="Age_Group", y="%Cure", color="Gender",
                  title="Ovarian Cancer - Cure % by Age Group")
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown( """ <h3 style='text-align:center; color:#00008B; font-family: Playfair Display;'> All You Need to Know About Ovarian Cancer </h3> """, unsafe_allow_html=True )

    with st.expander("Symptoms of Ovarian Cancer"):
        st.write("""
    • Abdominal bloating or swelling  
    • Pelvic or abdominal pain  
    • Feeling full quickly when eating  
    • Changes in bowel habits (constipation or diarrhea)  
    • Frequent urination or urgency  
    • Unexplained weight loss or gain  
    • Fatigue and weakness  
    • Back pain  
    """)


    with st.expander("Effects of Ovarian Cancer"):
        st.write("""
    • Discomfort or pain in abdomen and pelvis  
    • Fatigue and weakness  
    • Digestive problems (nausea, constipation, bloating)  
    • Fluid accumulation in abdomen (ascites)  
    • Weight changes and malnutrition  
    • Hormonal imbalance in some cases  
    • Reduced quality of life due to pain and fatigue  
    """)


    with st.expander("Causes of Ovarian Cancer"):
        st.write("""
    • Family history of ovarian or breast cancer  
    • Genetic mutations (BRCA1, BRCA2, and others)  
    • Age (more common after menopause)  
    • Hormonal factors (early menstruation, late menopause)  
    • Obesity  
    • Endometriosis in some cases  
    """)


    with st.expander("Treatments of Ovarian Cancer"):
        st.write("""
    • Surgery to remove one or both ovaries and nearby tissues  
    • Chemotherapy to kill cancer cells  
    • Targeted therapy for specific cancer types  
    • Radiation therapy in some cases  
    • Hormonal therapy  
    • Immunotherapy for certain cases  
    • Palliative care for symptom management  
    """)





# === Myeloma Cancer ===
elif cancer_type == "Myeloma Cancer":
    st.text("Myeloma (Multiple Myeloma) is a type of cancer that starts in the plasma cells, which are a kind of white blood cell found in the bone marrow. Plasma cells normally help fight infections by making antibodies.In this cancer, plasma cells grow uncontrollably, crowding out healthy blood cells and making abnormal proteins. This can damage the bones, kidneys, and immune system.")
    fig1 = px.funnel(df, x="Stage_of_Cancer", y="%Cure", color="Stage_of_Cancer",
                     title="📉 Myeloma Cancer - Cure % by Stage")
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.bar(df, x="Age_Group", y="Survival_Rate", color="Gender",
                  title="Myeloma Cancer - Survival Rate by Age Group")
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown( """ <h3 style='text-align:center; color:#00008B; font-family: Playfair Display;'> All You Need to Know About Myeloma Cancer </h3> """, unsafe_allow_html=True )

    with st.expander("Symptoms of Myeloma Cancer"):
        st.write("""
    • Bone pain, especially in the spine or ribs  
    • Fatigue and weakness  
    • Frequent infections  
    • Unexplained weight loss  
    • Nausea and constipation  
    • Excessive thirst and frequent urination  
    • Bruising or bleeding easily  
    • Anemia (low red blood cell count)  
    """)


    with st.expander("Effects of Myeloma Cancer"):
        st.write("""
    • Bone weakening and fractures  
    • Reduced kidney function  
    • Fatigue and weakness  
    • Increased risk of infections  
    • Anemia and low blood counts  
    • Hypercalcemia (high calcium levels) causing nausea, confusion  
    • Reduced quality of life due to pain and fatigue  
    """)


    with st.expander("Causes of Myeloma Cancer"):
        st.write("""
    • Genetic mutations in plasma cells  
    • Age (more common in people over 65)  
    • Family history of myeloma  
    • Exposure to radiation or certain chemicals  
    • Immune system disorders  
    • Gender and race (slightly more common in men and African Americans)  
    """)


    with st.expander("Treatments of Myeloma Cancer"):
        st.write("""
    • Chemotherapy to target cancer cells  
    • Targeted therapy (drugs that attack specific cancer cells)  
    • Immunotherapy to boost the immune system  
    • Stem cell transplant  
    • Radiation therapy for bone lesions  
    • Pain management and supportive care  
    • Lifestyle changes and nutritional support  
    """)






# === Stomache Cancer ===
elif cancer_type == "Stomache Cancer":
    st.text("Stomach cancer (Gastric cancer) is a type of cancer that starts in the stomach, the organ that helps break down and digest food.In this cancer, the cells of the stomach lining grow abnormally and uncontrollably, forming a tumor. It can spread to nearby organs and often develops slowly over many years")
    fig1 = px.histogram(df, x="Survival_Rate", color="Gender", nbins=10, barmode="overlay",
                        title="🍽 Stomach Cancer - Survival Rate Distribution")
    st.plotly_chart(fig1, use_container_width=True)
    fig2 = px.box(df, x="Stage_of_Cancer", y="%Cure", color="Gender",
                  title="Stomach Cancer - Cure % by Stage")
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown( """ <h3 style='text-align:center; color:#00008B; font-family: Playfair Display;'> All You Need to Know About Stomach Cancer </h3> """, unsafe_allow_html=True )

    with st.expander("Symptoms of Stomach Cancer"):
        st.write("""
    • Indigestion or heartburn  
    • Nausea and vomiting  
    • Stomach pain or discomfort  
    • Feeling full quickly after eating  
    • Unexplained weight loss  
    • Loss of appetite  
    • Fatigue and weakness  
    • Blood in vomit or stool  
    """)

# Effects of Stomach Cancer
    with st.expander("Effects of Stomach Cancer"):
        st.write("""
    • Difficulty eating and malnutrition  
    • Fatigue and weakness  
    • Pain and discomfort in the stomach  
    • Weight loss and muscle wasting  
    • Anemia due to bleeding  
    • Spread to other organs (metastasis)  
    • Reduced quality of life due to digestive issues  
    """)

# Causes of Stomach Cancer
    with st.expander("Causes of Stomach Cancer"):
        st.write("""
    • Infection with Helicobacter pylori (H. pylori)  
    • Smoking or tobacco use  
    • Family history of stomach cancer  
    • Diet high in salty, smoked, or processed foods  
    • Obesity  
    • Chronic gastritis or stomach inflammation  
    • Certain genetic mutations  
    """)

# Treatments of Stomach Cancer
    with st.expander("Treatments of Stomach Cancer"):
        st.write("""
    • Surgery to remove part or all of the stomach  
    • Chemotherapy to kill cancer cells  
    • Radiation therapy  
    • Targeted therapy for specific cancer types  
    • Immunotherapy to strengthen the immune response  
    • Palliative care to relieve symptoms  
    • Nutritional support and lifestyle changes  
    """)






# === Laryngeal Cancer ===
elif cancer_type == "Laryngeal Cancer":
    st.text("Laryngeal cancer is a type of cancer that starts in the larynx (voice box), the part of the throat that helps you speak, breathe, and swallow.In this cancer, the cells in the lining of the larynx grow abnormally and uncontrollably, forming a tumor. Since the larynx controls the voice, this cancer often affects speaking and breathing. Smoking and heavy alcohol use are the main risk factors.")
    fig1 = px.box(df, x="Gender", y="Survival_Rate", color="Gender", points="all",
                  title="🎤 Laryngeal Cancer - Survival Rate by Gender")
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.line(df, x="Age_Group", y="%Cure", color="Gender", markers=True,
                   title="Laryngeal Cancer - Cure % Trend by Age Group")
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown( """ <h3 style='text-align:center; color:#00008B; font-family: Playfair Display;'> All You Need to Know About Laryngeal Cancer </h3> """, unsafe_allow_html=True )

    with st.expander("Symptoms of Laryngeal Cancer"):
        st.write("""
    • Persistent hoarseness or voice changes  
    • Sore throat that doesn’t go away  
    • Difficulty swallowing  
    • Pain when swallowing  
    • Lump or swelling in the neck or throat  
    • Chronic cough  
    • Ear pain  
    • Unexplained weight loss  
    """)

# Effects of Laryngeal Cancer
    with st.expander("Effects of Laryngeal Cancer"):
        st.write("""
    • Difficulty speaking or loss of voice  
    • Trouble swallowing food and liquids  
    • Pain in throat or ear  
    • Fatigue and weakness  
    • Spread to nearby tissues or lymph nodes  
    • Reduced quality of life due to speech and swallowing issues  
    """)

# Causes of Laryngeal Cancer
    with st.expander("Causes of Laryngeal Cancer"):
        st.write("""
    • Smoking or tobacco use  
    • Heavy alcohol consumption  
    • Exposure to certain chemicals or fumes  
    • Human papillomavirus (HPV) infection  
    • Poor nutrition  
    • Chronic irritation of the larynx  
    • Age (more common in people over 55)  
    """)

# Treatments of Laryngeal Cancer
    with st.expander("Treatments of Laryngeal Cancer"):
        st.write("""
    • Surgery to remove part or all of the larynx  
    • Radiation therapy  
    • Chemotherapy  
    • Targeted therapy for specific cancer types  
    • Immunotherapy  
    • Speech and swallowing therapy after treatment  
    • Palliative care to manage symptoms  
    """)






# === Brain Cancer ===
elif cancer_type == "Brain Cancer":
    st.text("Brain cancer is a type of cancer that starts in the brain cells.In this cancer, abnormal cells in the brain grow uncontrollably and form a tumor. This tumor can press on different parts of the brain, affecting memory, movement, balance, vision, and other body functions. Brain cancer can spread within the brain and spinal cord but usually doesn’t spread to other parts of the body")
    fig1 = px.scatter(df, x="Survival_Rate", y="Death_Rate", size="%Cure",
                      color="Gender", hover_name="Stage_of_Cancer",
                      title="🧠 Brain Cancer - Survival vs Death Rate vs Cure %")
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.bar(df, x="Age_Group", y="Survival_Rate", color="Gender",
                  title="Brain Cancer - Survival Rate by Age Group")
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown( """ <h3 style='text-align:center; color:#00008B; font-family: Playfair Display;'> All You Need to Know About Brain Cancer </h3> """, unsafe_allow_html=True )

    with st.expander("Symptoms of Brain Cancer"):
        st.write("""
    • Persistent headaches, often worse in the morning  
    • Nausea and vomiting  
    • Seizures  
    • Changes in speech, vision, or hearing  
    • Balance or coordination problems  
    • Weakness or numbness in arms or legs  
    • Personality or behavior changes  
    • Fatigue and drowsiness  
    """)

# Effects of Brain Cancer
    with st.expander("Effects of Brain Cancer"):
        st.write("""
    • Cognitive and memory problems  
    • Difficulty walking or maintaining balance  
    • Muscle weakness or paralysis  
    • Seizures and convulsions  
    • Speech and language difficulties  
    • Headaches and nausea  
    • Fatigue and decreased quality of life  
    """)

# Causes of Brain Cancer
    with st.expander("Causes of Brain Cancer"):
        st.write("""
    • Genetic mutations in brain cells  
    • Exposure to radiation  
    • Family history of brain tumors  
    • Weak immune system  
    • Exposure to carcinogenic chemicals  
    • Certain hereditary syndromes (like Li-Fraumeni syndrome)  
    """)

# Treatments of Brain Cancer
    with st.expander("Treatments of Brain Cancer"):
        st.write("""
    • Surgery to remove the tumor  
    • Radiation therapy  
    • Chemotherapy  
    • Targeted therapy for specific tumor types  
    • Immunotherapy  
    • Palliative care to manage symptoms  
    • Rehabilitation therapy for speech, mobility, and cognition  
    """)






# === Acute Myeloid Leukemia ===
elif cancer_type == "Acute myeloid leukemia":
    st.text("Acute Myeloid Leukemia (AML) is a type of blood cancer that starts in the bone marrow, where new blood cells are made.In AML, the bone marrow makes too many immature white blood cells (called myeloblasts) that don’t work properly. These cells crowd out healthy blood cells, leading to problems like infections, anemia, and bleeding. AML develops quickly (acute) and needs early treatment")
    fig1 = px.line(df, x="Age_Group", y="%Cure", color="Gender", markers=True,
                   title="🩸 Acute Myeloid Leukemia - Cure % Trend by Age Group")
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.bar(df, x="Stage_of_Cancer", y="Survival_Rate", color="Gender",
                  barmode="group", text_auto=True,
                  title="Acute Myeloid Leukemia - Survival Rate by Stage")
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown( """ <h3 style='text-align:center; color:#00008B; font-family: Playfair Display;'> All You Need to Know About Acute Myeloid Leukemia Cancer </h3> """, unsafe_allow_html=True )

    with st.expander("Symptoms of Acute Myeloid Leukemia"):
        st.write("""
    • Fatigue and weakness  
    • Fever or frequent infections  
    • Unexplained weight loss  
    • Easy bruising or bleeding  
    • Nosebleeds or gum bleeding  
    • Shortness of breath  
    • Bone or joint pain  
    • Pale skin  
    """)

# Effects of Acute Myeloid Leukemia
    with st.expander("Effects of Acute Myeloid Leukemia"):
        st.write("""
    • Anemia (low red blood cells) causing fatigue  
    • Increased risk of infections due to low white blood cells  
    • Bleeding and bruising due to low platelets  
    • Weakness and fatigue  
    • Organ damage if leukemia spreads  
    • Reduced quality of life  
    """)

# Causes of Acute Myeloid Leukemia
    with st.expander("Causes of Acute Myeloid Leukemia"):
        st.write("""
    • Genetic mutations in bone marrow cells  
    • Exposure to high doses of radiation  
    • Previous chemotherapy or cancer treatment  
    • Smoking  
    • Certain chemical exposures (e.g., benzene)  
    • Blood disorders like myelodysplastic syndrome  
    • Family history of leukemia  
    """)

# Treatments of Acute Myeloid Leukemia
    with st.expander("Treatments of Acute Myeloid Leukemia"):
        st.write("""
    • Chemotherapy to destroy leukemia cells  
    • Targeted therapy for specific genetic mutations  
    • Stem cell transplant  
    • Radiation therapy in some cases  
    • Immunotherapy  
    • Supportive care for infections, anemia, and bleeding  
    • Lifestyle and nutritional support during treatment  
    """)






# === Breast Cancer ===
elif cancer_type == "Breast Cancer":
    st.text("Breast cancer is a type of cancer that starts in the breast tissue, usually in the milk ducts or milk-producing glands (lobules).In this cancer, the breast cells grow abnormally and uncontrollably, forming a lump or tumor. It can spread to nearby tissues or other parts of the body if not treated early. Breast cancer is one of the most common cancers in women, but men can also get it.")
    
    fig1 = px.pie(df, names="Gender", values="%Cure", hole=0.4,
                  title="🎀 Breast Cancer - Cure % Distribution by Gender")
    st.plotly_chart(fig1, use_container_width=True)


    radar_data = df.melt(id_vars=["Gender"], 
                         value_vars=["Survival_Rate", "Death_Rate"],
                         var_name="Metric", value_name="Value")
    fig2 = px.line_polar(radar_data, r="Value", theta="Metric", color="Gender", line_close=True,
                         title="Breast Cancer - Survival vs Death Rate Radar")
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown( """ <h3 style='text-align:center; color:#00008B; font-family: Playfair Display;'> All You Need to Know About Breast Cancer </h3> """, unsafe_allow_html=True )

    with st.expander("Symptoms of Breast Cancer"):
        st.write("""
    • Lump or thickening in the breast or underarm  
    • Change in breast size or shape  
    • Skin dimpling or puckering  
    • Nipple discharge other than breast milk  
    • Redness or scaling of the nipple or breast skin  
    • Pain in the breast or nipple  
    • Swelling in part of the breast  
    """)

# Effects of Breast Cancer
    with st.expander("Effects of Breast Cancer"):
        st.write("""
    • Physical changes in the breast or chest  
    • Pain and discomfort  
    • Swelling and inflammation  
    • Fatigue and weakness  
    • Emotional and psychological impact  
    • Spread to lymph nodes or other organs (metastasis)  
    • Reduced quality of life  
    """)

# Causes of Breast Cancer
    with st.expander("Causes of Breast Cancer"):
        st.write("""
    • Genetic mutations (BRCA1, BRCA2)  
    • Family history of breast cancer  
    • Hormonal factors (early menstruation, late menopause)  
    • Obesity and sedentary lifestyle  
    • Alcohol consumption  
    • Age (risk increases with age)  
    • Exposure to radiation  
    """)

# Treatments of Breast Cancer
    with st.expander("Treatments of Breast Cancer"):
        st.write("""
    • Surgery (lumpectomy or mastectomy)  
    • Radiation therapy  
    • Chemotherapy  
    • Hormone therapy  
    • Targeted therapy  
    • Immunotherapy in specific cases  
    • Palliative care for symptom relief  
    """)









# === Skin Cancer ===
elif cancer_type == "Skin Cancer":
    st.text("Skin cancer is a type of cancer that starts in the skin cells.In this cancer, the skin cells grow abnormally and uncontrollably, usually because of too much exposure to the sun’s ultraviolet (UV) rays or tanning beds. It is the most common type of cancer but also one of the most preventable. There are different types, such as basal cell carcinoma, squamous cell carcinoma, and melanoma.")
    
    fig1 = px.density_heatmap(df, x="Age_Group", y="Survival_Rate", z="Death_Rate",
                              color_continuous_scale="Viridis",
                              title="☀ Skin Cancer - Survival vs Death Rate Heatmap")
    st.plotly_chart(fig1, use_container_width=True)

    
    fig2 = px.scatter(df, x="Stage_of_Cancer", y="%Cure", size="Survival_Rate",
                      color="Gender", hover_name="Age_Group",
                      title="Skin Cancer - Cure % vs Stage (Bubble Chart)")
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown( """ <h3 style='text-align:center; color:#00008B; font-family: Playfair Display;'> All You Need to Know About Skin Cancer </h3> """, unsafe_allow_html=True )


    with st.expander("Symptoms of Skin Cancer"):
        st.write("""
    • New growths or sores that don’t heal  
    • Changes in existing moles (size, shape, color)  
    • Itching, tenderness, or pain in a mole or spot  
    • Redness or swelling beyond the mole  
    • Oozing or bleeding from a mole or lesion  
    • Rough, scaly patches on the skin  
    • Dark streaks under nails (for subungual melanoma)  
    """)

# Effects of Skin Cancer
    with st.expander("Effects of Skin Cancer"):
        st.write("""
    • Disfigurement or changes in skin appearance  
    • Pain or discomfort in affected areas  
    • Spread to lymph nodes or other organs (metastasis)  
    • Fatigue and weakness  
    • Emotional and psychological impact  
    • Increased risk of additional skin cancers  
    """)

# Causes of Skin Cancer
    with st.expander("Causes of Skin Cancer"):
        st.write("""
    • Excessive exposure to UV radiation from the sun or tanning beds  
    • Fair skin, freckling, and light hair or eye color  
    • Family history of skin cancer  
    • Certain genetic mutations  
    • Exposure to chemical carcinogens  
    • Weakened immune system  
    """)

# Treatments of Skin Cancer
    with st.expander("Treatments of Skin Cancer"):
        st.write("""
    • Surgical removal of cancerous lesions  
    • Cryotherapy (freezing abnormal cells)  
    • Radiation therapy  
    • Chemotherapy for advanced cases  
    • Targeted therapy for specific mutations  
    • Immunotherapy  
    • Palliative care for symptom management  
    """)








# === Bone Cancer ===
elif cancer_type == "Bone Cancer":
    st.text("Bone cancer is a type of cancer that starts in the bones.In this cancer, the bone cells grow abnormally and uncontrollably, forming a tumor inside the bone. It can weaken the bone, cause pain, swelling, and sometimes fractures. Bone cancer may begin in the bone itself (primary bone cancer) or spread to the bone from other cancers (secondary bone cancer)")
    
    fig1 = px.scatter_3d(df, x="%Cure", y="Survival_Rate", z="Death_Rate",
                         color="Gender", symbol="Stage_of_Cancer",
                         title="🦴 Bone Cancer - 3D Analysis (%Cure, Survival, Death)")
    st.plotly_chart(fig1, use_container_width=True)

    
    fig2 = px.funnel_area(df, names="Stage_of_Cancer", values="Survival_Rate",
                          title="Bone Cancer - Survival Rate by Stage (Funnel Area)")
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown( """ <h3 style='text-align:center; color:#00008B; font-family: Playfair Display;'> All You Need to Know About Bone Cancer </h3> """, unsafe_allow_html=True )

    with st.expander("Symptoms of Bone Cancer"):
        st.write("""
    • Persistent bone pain, often worsening at night  
    • Swelling or tenderness near the affected bone  
    • Fractures with minor injury  
    • Fatigue and weakness  
    • Unexplained weight loss  
    • Reduced mobility or difficulty moving limbs  
    • Numbness or tingling if tumor presses on nerves  
    """)

# Effects of Bone Cancer
    with st.expander("Effects of Bone Cancer"):
        st.write("""
    • Weakening of bones and increased risk of fractures  
    • Pain and discomfort  
    • Reduced mobility and physical function  
    • Fatigue and overall weakness  
    • Spread to other bones or organs (metastasis)  
    • Reduced quality of life  
    """)

# Causes of Bone Cancer
    with st.expander("Causes of Bone Cancer"):
        st.write("""
    • Genetic mutations in bone cells  
    • Previous radiation therapy  
    • Family history of bone cancer  
    • Paget’s disease of bone (rare)  
    • Certain inherited syndromes  
    • Exposure to carcinogenic chemicals  
    """)

# Treatments of Bone Cancer
    with st.expander("Treatments of Bone Cancer"):
        st.write("""
    • Surgery to remove the tumor  
    • Radiation therapy  
    • Chemotherapy  
    • Targeted therapy for specific cancer types  
    • Immunotherapy in certain cases  
    • Pain management and supportive care  
    • Physical therapy and rehabilitation  
    """)








# === Retinoblastoma Cancer ===
elif cancer_type == "Retinoblastoma Cancer":
    st.text("Retinoblastoma is a rare type of cancer that starts in the retina, the light-sensitive tissue at the back of the eye. It usually affects young children, often before the age of 5.In this cancer, the cells of the retina grow abnormally and uncontrollably, forming a tumor. This can affect vision and, if not treated early, may spread to other parts of the body")

    fig1 = px.sunburst(df, path=["Stage_of_Cancer", "Gender"], values="Survival_Rate",
                       title="👁 Retinoblastoma - Survival Rate by Stage & Gender")
    st.plotly_chart(fig1, use_container_width=True)

    
    fig2 = px.bar_polar(df, r="%Cure", theta="Age_Group", color="Gender",
                        title="Retinoblastoma - Cure % by Age Group (Polar Bar)")
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown( """ <h3 style='text-align:center; color:#00008B; font-family: Playfair Display;'> All You Need to Know About Retinoblastoma Cancer </h3> """, unsafe_allow_html=True )


    with st.expander("Symptoms of Retinoblastoma"):
        st.write("""
    • White color in the pupil (leukocoria)  
    • Eye redness or swelling  
    • Crossed eyes (strabismus)  
    • Poor vision or vision loss  
    • Eye pain in some cases  
    • Changes in eye color or appearance  
    """)

# Effects of Retinoblastoma
    with st.expander("Effects of Retinoblastoma"):
        st.write("""
    • Vision impairment or blindness in affected eye  
    • Eye pain and discomfort  
    • Swelling and redness of the eye  
    • Spread of cancer to surrounding tissues or brain in advanced cases  
    • Emotional impact on child and family  
    """)

# Causes of Retinoblastoma
    with st.expander("Causes of Retinoblastoma"):
        st.write("""
    • Genetic mutations in the RB1 gene  
    • Inherited family history of retinoblastoma  
    • Sporadic mutations without family history  
    • Rarely associated with other genetic syndromes  
    """)

# Treatments of Retinoblastoma
    with st.expander("Treatments of Retinoblastoma"):
        st.write("""
    • Surgery to remove tumor or affected eye in severe cases  
    • Chemotherapy to shrink tumor  
    • Radiation therapy for localized tumors  
    • Laser therapy or cryotherapy to destroy tumor cells  
    • Targeted therapy in specific cases  
    • Vision rehabilitation and supportive care  
    """)



    
