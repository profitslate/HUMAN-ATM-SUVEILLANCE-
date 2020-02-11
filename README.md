<h5>ATM SMART SECURITY</h5>

<h5>Goal</h5>
Our goal is to secure those atm’s where there no security guard and have only one machine available(mean small atm’s). 
The system is mainly to ensure that there is a proper human and machine interaction happening. It will ensure that no one 
is hiding his face or trying to, attach any machines in the atm.

<h5>How It Works</h5>
<li>First, it will check for human counts</li>
<li>it will check for human faces</li>
<li>If the face count and the human count is not the same, it will ask for remove any kind of cover that the person has
If not removed then the system will go for threat detection where it will start looking for helmet or any kind of mask.</li>
<li>If threat detected then the system will look the doors. And report to the nearest authority.</li>
<li>If no threat is detected it will start again from the beginning and look the door to ensure nothing going wrong in our side, and it will try for 5 times and then permanently lock the door.</li>

<img src="https://github.com/tutoraddicts/ATM_SMART_SEQURITY/blob/v1.0/flow_chart.png">

Here atm_main.py is the main file
<h1>
    Pre Requirements
</h1>
<h5>
    Main requirements
</h5>
<ul>
    <li><a href="https://www.python.org/">python/python3</a></li>
    <li><a href="https://www.python.org/">python-pip/pyhton3-pip</a></li>
    <li><a href="https://opencv.org/">python3-opencv</a></li>
</ul>
<h5>
    Python Libraries We need
</h5>
<ul>
    <li><a href="https://cmake.org/">cmake</a></li>
    <li><a href="http://dlib.net/">dlib</a></li>
    <li><a href="https://imageai.readthedocs.io/en/latest/">imageai</a></li>
    <li><a href="https://www.tensorflow.org/">tensorflow</a></li>
    <li><a href="https://www.tensorflow.org/guide/gpu">tensorflow-gpu</a></li>
    <li><a href="https://numpy.org/">numpy</a></li>
    <li><a href="https://github.com/ageitgey/face_recognition">face_recognition</a></li>
</ul>
<h1>
    How To Start This Application
</h1>

<h5>
    atm_main is the main file to run this application just<br/>
    use this command in the same directory<br/>
    <h3><code>python3 atm_main.py</code></h3>
</h5>

<h1>
Download Requirements
</h1>
<h5>
    You need Two requirements
    <ul>
        <li><a href="https://github.com/profitslate/HUMAN-ATM-SUVEILLANCE-/releases/download/V0.1/detection_model-ex-063--loss-0009.921.h5">YOLOV3 MODEL</a></li>
        <li><a href="https://github.com/profitslate/HUMAN-ATM-SUVEILLANCE-/releases/download/V0.1/detection_config.json">JSON File</a></li>
    </ul> 
</h5>
