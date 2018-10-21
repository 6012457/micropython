
html_header= """
<!DOCTYPE html PUBLIC "-//WAPFORUM//DTD XHTML Mobile 1.0//EN" "http://www.wapforum.org/DTD/xhtml-mobile10.dtd">
<html>
<head>
<title>Botdemy MicroPython IoT Car</title>
<style>
body {background-color: white}
h1 {color:red}
button {
        color: red;
        height: 100px;
        width: 100px;
        background:white;
        border: 3px solid #4CAF50; /* Green */
        border-radius: 50%;
        font-size: 150%;
        position: center;
}
</style>
</head>
<body>
<center><h1>
servo
"""
html_body="""</h1>
<form>
<div>
<button name="CMD" value="add" type="submit">add</button>
<button name="CMD" value="forward" type="submit">Forward</button>
<button name="CMD" value="dec" type="submit">dec</button></div>
<div><button name="CMD" value="left" type="submit">Left</button>
<button name="CMD" value="stop" type="submit">Stop</button>
<button name="CMD" value="right" type="submit">Right</button></div>
<div><button name="CMD" value="cadd" type="submit">cadd</button>
<button name="CMD" value="back" type="submit">Back</button>
<button name="CMD" value="cdec" type="submit">cdec</button>
<div><button name="CMD" value="center" type="submit">center</button></div>
</div>
"""
html_end="""
</form>
</center>
</body>
</html>


"""
