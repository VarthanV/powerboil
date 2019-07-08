HTML_STRING= """<!DOCTYPE html>
<html lang="en">
<head>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <link rel="shortcut icon" type="image/png" href=  " https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpq_BhX36ZR3khblEmfr_fisFhix-gtCzQiH6whD2z4w3QfkaTpQ"/>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
     <title> {0} </title>
</head>
<body>
   <h1 style="text-align: center"> {1}   </h1> 
   <div class="container">
        <p class="lead">  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ac orci phasellus egestas tellus. Convallis tellus id interdum velit laoreet. Quam viverra orci sagittis eu volutpat odio facilisis. Id diam maecenas ultricies mi eget mauris. Laoreet suspendisse interdum consectetur libero id faucibus nisl tincidunt. Rhoncus aenean vel elit scelerisque mauris. Vulputate mi sit amet mauris commodo quis imperdiet massa tincidunt. Sit amet nisl suscipit adipiscing bibendum. Donec adipiscing tristique risus nec feugiat in fermentum posuere. Gravida rutrum quisque non tellus orci ac auctor</p>

   </div>
   
  
   <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
   <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
   <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>  
</body>
</html>"""

readme = """ ## {} \n  {} A {} project  """
extension_html="""     
<!DOCTYPE html>
<html>
  <head>
    <title>{}</title>
    <link
      href="https://fonts.googleapis.com/css?family=Roboto"
      rel="stylesheet"
      type="text/css"
    />
    <link
      href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
      rel="stylesheet"
      integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN"
      crossorigin="anonymous"
    />
    <style>
  
      html,
      body {
        font-family: "Roboto", sans-serif;
        font-size: 14px;
        margin: 0;
        min-height: 180px;
        padding: 0;
        width: 384px;
      }
      h1 {
        font-family: "Roboto", monospace;
        font-size: 22px;
        font-weight: 400;
        margin: 0;
        color:royalblue;
      }
     
      .modal-content {
        padding: 0 22px;
        text-align: center;
        font-size: 30px;
      }
   
      .logo {
        padding: 16px;
      }
    
      
     
     
    </style>
    <script src="popup.js"></script>
  </head>

  <body>
    <div class="modal-header">
      <h1 class="logo" style="text-align: center;">
         {}
      </h1>
    </div>
    <div class="modal-content">
      <h1 id ="text"></h1>
    </div>
    <script src="popup.js"></script>
  </body>
</html>

"""  
popupfile ="""
function disp() {
    document.getElementById('text').innerHTML = Sample Chrome Extension Project ;
}

window.addEventListener('load', disp());
"""
linearRegression ="""
import numpy as np
from sklearn.linearmodel import LinearRegression
X=np.array([[1,1],[1,2],[2,3]])
Y = np.dot(X, np.array([1, 2])) + 3
linear=LinearRegression()
model=linear.fit(X,Y)
print(model.score(X,Y))
"""
basic_plot = """
import matplotlib.pyplot as plt
import numpy as np
X=np.arange(10)
Y= np.square(np.arange(10))
plt.plot(X,Y)
plt.title(" Number vs Square")
plt.xlabel(" Number")
plt.ylabel("Square of the Number (X * x)")
plt.show()
plt.savefig('sample.png')
 """

