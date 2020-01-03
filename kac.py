k =open("kanchan.html","w")
a= """<!doctype html>
<html>
 <head>
<title>RESUME</title>
<style type="text/css">
    table {
        font-size: 18px;
    }
    #heading{
        font-size: 20px;
        }
</style>
</head>
<body style="padding-top: 5%; padding-left:15%; padding-right:15%; ">
    <div class="col-xs-6"  >

<div>
  <center><h1><u><b> RESUME</u></b></h1></center>  
<h3>Kanchan Bawariya </h3>
<p > preetibwr03@gmail.com</p>
<p>DOB: 03 June 2000</p>
<p>Narayan Nagar Bhopal</p
<p>Contact No.: 7389030668</p>
 
  <h3><u><b>CAREER OBJECTIVE</u></b></h3>
  <p>To secure a position where I can efficiently contribute my skills and abilities to the growth of the organization and build my professional career.</p>
            <h3><u><b>EDUCATION </b></u></h3>
            <table border="1" class="table ">
                <tr class="table-primary">
                    <th>Qualification</th>
                    <th>Institute</th>
                    <th>Percentage / Grades</th>
                    <th>Year</th>
                </tr>
                <tr>
                    <td>10th</td>
                    <td>Flower Vale Higher Secondary School Jhurrey</td>
                    <td>79.5%</td>
                    <td>2015</td>
                </tr>
                <tr>
                    <td>12th</td>
                    <td> Govt. Kanya Shiksha Parisar Higher Secondary<br> School Chhindwara</td>
                    <td>67.4%</td>
                    <td>2017</td>
                </tr>
                <tr>
                    <td>1st Sem</td>
                    <td>Barkatullah University Institute<br> Of Technology Bhopal</td>
                    <td>7.52 SGPA</td>
                    <td>2019</td>
                </tr>
                <tr>
                    <td>2nd Sem</td>
                    <td>Barkatullah University Institute<br> Of Technology Bhopal</td>
                    <td>7.58 SGPA</td>
                    <td>2019</td>
                </tr>
                
            </table>

        </div>
          <h3 style="text-transform: uppercase;"><u>Key Skills</u></h3>
     <ol>
<h3> <li> C++</h3>
</li>
   <h3><li> C</h3>
   </li>

         <h3 style="text-transform: uppercase;"><li> html</h3>
              </li>
      <h3><li> MySql</h3>
               </li>
        </ol>

    <h3><b><u style="text-transform: uppercase;">Langauges</u></b></h3>
    <ol style="font-size: 25px;">
        <li> English</li>
        <li>Hindi</li>
    </ol>
    <h3><u><b style="text-transform: uppercase;">Persnol Profile ID</b></u></h3>
    <ol style="font-size: 25px;">
        <li>Github :  Kanchanbawariya0306</a></li>
        <li>Linkdin :  preetibwr03@gmail.com</a></li>
       <li>HackerRank :preetibwr03@gmail.com</a></li>
       <li>Canvas :  preetibwr03@gmail.com</a></li> 
       <li>Intershala :  preetibwr03@gmail.com</a></li></ol>    
        <h3><u><b>WORK  EXPERIENCE</u></b></h3>
        <p style="font-size: 20px;">Fresher</p>
</div></body>
</html>"""
k.write(a)
k.close()
