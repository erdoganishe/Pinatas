# Pinatas



# Realistion:

To solve this task used 3 methods.

  ## Bruteforce method ~1,5 hours

  We just try all possible orders of removing element, and get max result. Works on every array (list in our case) lenght and always correct, but time complexity is O(n) = n^2*n!, which is terrible, and works too long for 10+ elements.

  ## NN method ~6 hours

  For this one I tried to use NN.

  Idea is to get list at input and get index of element that should be destroyed.
  
  Train dataset was collected using Dataset_fill.ipynb script by saving result of bruteforce method for random elements, and saves index of first removing.
  Dataset ~100000 lines. 
  There was a problem with collection data, because to get data with long(8+) arrays I must wait too long, so max value for list in this method - 7.

  You can see how NN train and testing at nn_training and testing folder 
  
  This method has one more problem, using 4+ digits numbers will make an error, because all training dataset was for elements not more 1000, and index will be out of bounds.
  
  Overall, this method works corrert for ~25% random examples.

  Biggest problem was at last 3 elements, so it inspired me to do combined method.

  ## Combined method ~1 hour

  It uses NN while 3 elements left, then use bruteforce method, which garantee correct results.

  It is better variant, and has ~45% correct answers for random examples.

  NN and Combined methods can`t garantee correct result, but at least I tried to use machine learning to solve this task.


  You need Installed Py for running this.
  To run code u must do following steps (for Windows):

  ### Preinstallations:
  
    venv\Scripts\activate
 
    pip intall -r requirements.txt
    
  ### For bruteforce method:
  
    py pinatas.py {array you want to parse}
    
  ### For other methods:
  
    py test_with_nn.py {array you want to parse} 


  
