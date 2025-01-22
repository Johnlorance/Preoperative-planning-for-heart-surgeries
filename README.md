# Development of an AI-Based Website for Automated Pre-Operative Planning in Aortic Valve Replacement Using Deep Learning
## 🌟 Overview
This pipeline introduces an AI-web-based software to help perform minimally invasive aortic valve replacement (AVR) procedures. The complete pipeline contains three main steps or deep learnign models: aortic
extraction, automatic landmark detection, and calculation of the specific measurements required for valve replacement. 
For Computed Tomography Angiography (CTA) scans, separate deep neural network models based on the U-Net architecture in the Medical Open Network for AI (MONAI) framework segment out key anatomical landmarks,
including the Sinotubular Junction (STJ), Left Coronary Artery (LCA), Right Coronary Artery (RCA), and Annulus Plane. 
This improves the accuracy of aorta segmentation and landmark detection. A web interface facilitates easy data upload, visualization of segmentation results, and access to key measurements for preoperative planning.
Artificial Intelligence (AI) and machine learning in medical imaging lead to more accurate preoperative planning of Transcatheter Aortic Valve Replacement (TAVR) procedures, reducing the likelihood of complications
from improperly fitted valves.
There is still more work to be done before the model can be used in cardiovascular disease diagnosis, including refining models, enriching datasets, and integrating several features
that are beneficial for cardiologists.
