# Test Python
## Task text

These are deviations of floor vs ceiling corners of one of our models with ground truth labels for the room name and number of corners in that room with predictions. Please create meaningful statistics of how well the model performed. 
 
Gt_corners = ground truth number of corners in the room 
 
Rb_corners = number of corners found by the model 
 
Mean max min and all others are deviation values in degrees. 
 
Create project in idea, pycharm or vscode 
 
Create requirements.txt and virtual env 
 
Create class for drawing plots 
 
Create function “draw_plots” 
 
→ reads json file passed as parameter as a pandas dataframe 
 
→ draws plot for comparing different columns 
 
→ saves plots in a folder called “plots” 
 
→ returns paths to all plots 
 
Create jupyter notebook called Notebook.ipynb in the root directory to call and visualize our plots


## Summary

After analyzing the data, I came to the conclusion that the model does not work well, despite the fact that all true values coincided with the predicted values.  The data had a wide range of values, for example, a room with four corners was determined to be true even at values that I considered an outlier, since they were very different from the average or median values.  This could happen if this data sample is a training one.   Overfitting could have occurred; the model simply remembered the values of each room and cannot work correctly on other values.  This can be seen in the graph, despite the fact that the maximum values are similar for each of the angle values, I think that this is not enough to accurately determine the true angle.


