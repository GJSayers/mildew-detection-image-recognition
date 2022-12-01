# Mildew Detection in Cherry Leaves - Image Recognition Project

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.



## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis 
* 1- We suggest that images of Cherry leaves with powdery mildew will have enough differences compared to those without the disease in order to train the model with an image dataset.
* 2- A company analysis showed that it takes 30 minutes to evaluate a Cherry tree manually for signs of powdery Mildew.  We propose that using image recognition will produce a vast time-benefit for the company and ensure that the detection of mildew is scalable. 
* 3- Since the sample dataset provided contains images classified into infected vs uninfected, we suggest that binary classification will be the best way to determine the difference between infected and uninftected leaves.  

## Validation of Hypothesis
* 1- The dataset will be analysed, using test, train and validation techniques to investigate image recognition accuracy.
* 2- Validation process will be displayed in the dashboad
* 3- Upload of images to determine infection will be included in the dashboard. 


## The rationale to map the business requirements to the Data Visualisations and ML tasks
* **Business Requirement 1**: Data Visualization 
	* We will display the "mean" and "standard deviation" images for infected vs uninfected leaves.
 	* We will display the difference between an average infected leaf and an average uninfected leaf.
	* We will display a image montage for either infected or uninfected leaves.

* **Business Requirement 2**:  Classification
	* We want to predict if a given leaf is infected or not with powdery mildew. 
	* We want to build a binary classifier and generate reports.



## ML Business Case
* We want a ML model to predict if a leaf is infected with powdery mildew or not, based on historical image data. It is a supervised model, a 2-class, single-label, classification model.
* Our ideal outcome is provide the team at Farmy foods a faster method of determining if a plant is infected with powdery mildew or not.
* The model success metrics are
	* Accuracy of 65% or above on the test set.
* The model output is defined as a flag, indicating if the leaf is infected with powdery mildew or not. The farm staff will do the leaf inspection as usual and upload the picture to the App. The prediction is made on the fly (not in batches).
* Heuristics: The current process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. Currently staff would need to be trained to spot the signs in detail, but with image analysis, sample collection and processing will be quicker and could be performed by staff with less expertise or potentially robotically at scale.
* The training data to fit the model come from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). This dataset contains about 4+ thousand images. 
	* Train data - target: infected or not; features: all images.


## Dashboard Design
## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick Project Summary
* Quick project summary
	* General Information
		* Powdery Mildew is a disease infecting herbaceous and woody plants, and can result in a low fruit yield in the case of Cherry Trees.
		* The current process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. 
		* According to the Conneticut Portal:  Powdery mildews are easily recognized by the white, powdery growth of the fungus on infected portions of the plant host. The powdery appearance results from the superficial growth of the fungus as thread-like strands (hyphae) over the plant surface and the production of chains of spores (conidia). Colonies vary in appearance from fluffy and white to sparse and gray. 
	* Project Dataset
		* The available dataset contains 2104 out of +4 thousand images taken from images of infected leaves.
	* Link to additional information
	* Business requirements
		*  The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
		*  The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

### Page 2: Infected Leaves Visualizer
* It will answer business requirement 1
	* Checkbox 1 - Difference between average and variability image
	* Checkbox 2 - Differences between average infected and average uninfected leaves.
	* Checkbox 3 - Image Montage

### Page 3: Powdery Mildew Detector
* Business requirement 2 information - "The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew."
* Link to download a set of infected and uninfected leaves for live prediction.
* User Interface with a file uploader widget. The user should upload multiple leaf sample images. It will display the image and a prediction statement, indicating if the leaf is infected or not with powdery mildew and the probability associated with this statement. 
* Table with image name and prediction results.
* Download button to download table.

### Page 4: Project Hypothesis and Validation
* Block for each project hypothesis, describe the conclusion and how it is validated.

### Page 5: ML Performance Metrics
* Label Frequencies for Train, Validation and Test Sets
* Model History - Accuracy and Losses
* Model evaluation result

## Unfixed Bugs
* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from [The Connecticut Agricultural Experiment Station](https://portal.ct.gov/CAES/Fact-Sheets/Plant-Pathology/Powdery-Mildew)
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.



## Acknowledgements (optional)
* Thank the people that provided support throughout this project.
