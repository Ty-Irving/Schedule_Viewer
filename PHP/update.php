<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel = "stylesheet" href = "../CSS/styles.css"/>
    <title>Update Info</title>
</head>
<body>
    <div class = "header">
        <a href = "../PHP/schedule_view.php"><img class = "header-img" src = "https://cdn.iconscout.com/icon/free/png-256/timer-83-470366.png"></a>
        <div class = "header-info">
            <a class = "header-link" href="../PHP/update.php" style = "background-color: rgba(0, 136, 107, 0.768)"> UPDATE INFO</a>
            <a class = "header-link" href = "../PHP/schedule_view.php">SCHEDULE VIEW</a>
            <a class = "header-link" href = "../PHP/index.php">LOGOUT</a>
        </div>
    </div>

    <div class = "builder-startup" id = "startup">
        <div class = "builder-startup-content">
            <img src = "../PHP/user-img.png" class = "startup-img">
            <p>Type Login </p>
            <input type = "text" placeholder = "Username...">
            <input type = "password" placeholder ="Password...">

            <button onclick="hideStartup()">LOGIN</button>
        </div>    
    </div>

    <div class = "update" id = "update">
        <div class = "update-content">
            <h1>Type New Info</h1>
            <input type = "text" placeholder = "First Name...">
            <input type = "text" placeholder = "Last Name...">
            <input type = "text" placeholder = "Address...">
            <input type = "text" placeholder = "Username...">
            <input type = "password" placeholder = "New Password...">
            <input type = "password" placeholder = "Confirm Password...">
            <button onclick = "showStartup()">UPDATE INFO</button>
        </div>
    </div>
    
   
</body>
</html>


<script type="text/javascript">
    const STARTUP = document.getElementById("startup");
    const UPDATE = document.getElementById("update");

    function hideStartup()
    {
        STARTUP.style.display='none';
        showUpdate();
    }

    function showStartup()
    {
        STARTUP.style.display="block";
        hideUpdate();
    }

    function hideUpdate()
    {
        UPDATE.style.display="none";
    }

    function showUpdate()
    {
        UPDATE.style.display="block";
    }

</script>

<style type="text/css">
    h1
    {
        color: white;
        text-align: center;
    }

    .update
    {
        padding-top: 10%;
        display: none;
    }

    .update-content
    {
        width: 300px;
        height: 400px;
        background-color: #3c454f;
        border: black 1px solid;
        margin-left: auto;
        margin-right: auto;
    }

    img
    {
        filter: invert();
    }

    .builder-startup
    {
        padding-top: 10%;
    }

    input {
        width: 88%;
        margin: 15px;
        margin-top: 5px;
    }
    
    .builder-startup-content {
        margin-right: auto;
        margin-left: auto;
        width: 300px;
        min-width: 300px;
        height: 400px;
        background-color: #3c454f;
        border: black 1px solid;
    
    }
    
    .builder-startup-content p {
        margin-top: 50px;
        color: white;
        margin-left: 32%;
        font-size: 20px;
        font-weight: bold;
    }
    
    .builder-startup-content img {
        width: 60px;
        height: 60px;
        margin-top: 30px;
        margin-left: 40%;
    }
    
    button {
        width: 90%;
        margin-left: 15px;
        padding: 10px;
        opacity: 0.8;
        background-color: #04AA6D;
        border: none;
        color: white;
        font-weight: bold;
        margin-top: 15px;
    }

    .builder-startup-content button:hover {
        opacity: 1;
        cursor: pointer;
    }
</style>