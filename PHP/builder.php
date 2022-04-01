<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel = "stylesheet" href = "../CSS/styles.css"/>
    <title>Schedule Builder</title>
</head>
<body>

    <div class = "header">
        <a href = "../PHP/builder.php"><img class = "header-img" src = "https://cdn.iconscout.com/icon/free/png-256/timer-83-470366.png"></a>
        <div class = "header-info">
            <a class = "header-link" id = "header-link-1" href = "../PHP/departments.php">MANAGE DEPT</a>
            <a class = "header-link" id = "header-link-2" href = "../PHP/requests.php">REQUESTS</a>
            <a class = "header-link" id = "header-link-3" href = "../PHP/builder.php" style = "background-color: rgba(0, 136, 107, 0.768)">BUILDER</a>
            <a class = "header-link" id = "header-link-4" href = "../PHP/index.php">LOGOUT</a>
        </div>
    </div>

    <div class = "builder-startup" id = "startup">
        <div class = builder-startup-content>
            <img src = "../PHP/user-img.png" class = "startup-img">
            <p>Select User ID</p>
            <input list = "user" class = "user-list">
            <datalist id = "user">
                <option>user123</option>
                <option>user432</option>
                <option>user345</option>
                <option>user643</option>
            </datalist>
            <button onclick="hideStartup()">SETUP SCHEDULE</button>
        </div>
        
    </div>
    
    <div class = "builder-content" id = "builder">
        <img class = "schedule-img" src="../PHP/calender.png">
        <input type = "date" min = "2022-01-01" max = "2023-12-31">
        <input list = "time" placeholder="Start Time...">
        
        <input list = "time" placeholder="End Time...">
        <datalist id = "time">
            <option>7:00AM</option>
            <option>7:30AM</option>
            <option>8:00AM</option>
            <option>8:30AM</option>
            <option>9:00AM</option>
            <option>9:30AM</option>
            <option>10:00AM</option>
            <option>11:30AM</option>
            <option>12:00PM</option>
            <option>12:30PM</option>
            <option>1:00PM</option>
            <option>1:30PM</option>
            <option>2:00PM</option>
            <option>2:30PM</option>
            <option>3:00PM</option>
            <option>3:30PM</option>
            <option>4:00PM</option>
            <option>4:30PM</option>
            <option>5:00PM</option>
            <option>5:30PM</option>
            <option>6:00PM</option>
            <option>6:30PM</option>
            <option>7:00PM</option>
            <option>7:30PM</option>
        </datalist>

        <button onclick="showStartup()">SCHEDULE</button>
    </div>


</body>
</html>

<script type="text/javascript">
    const STARTUP = document.getElementById("startup");
    const BUILDER = document.getElementById("builder");

    function hideStartup()
    {
        STARTUP.style.display='none';
        showBuilder();
    }

    function showStartup()
    {
        STARTUP.style.display="block";
        hideBuilder();
    }

    function hideBuilder()
    {
        BUILDER.style.display="none";
    }

    function showBuilder()
    {
        BUILDER.style.display="block";
    }

</script>

<style type="text/css">
    
    .startup-img
    {
        filter: invert();
    }

    .schedule-img
    {
        width: 100px;
        margin-bottom: 40px;
        margin-top: 25px;
        margin-left: 38%;
        filter: invert();
    }
    .builder-startup 
    {
        padding-top: 10%;
    }
    
    input
    {
        width: 250px;
        height: 30px;
        margin-left: auto;
        margin-right: auto;
        margin-top: 20px;
        display: block;
    }

    .builder-startup-content input {
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
        margin-left: 25%;
        font-size: 20px;
        font-weight: bold;
    }
    
    .builder-startup-content img {
        width: 60px;
        height: 60px;
        margin-top: 30px;
        margin-left: 40%;
    }
    
    .builder-startup-content button {
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

    .builder-content {
        width: 400px;
        height: 500px;
        margin-top: 10%;
        background-color: #3c454f;
        margin-left: auto;
        margin-right: auto;
        color: white;
        border: black 1px solid;
        display: none;

    }
    
    .builder-content button
    {
        margin-top: 80px;
        width: 95%;
        margin-left: 10px;
        height: 40px;
        font-size: 20px;
        background-color: #04AA6D;
        border: none;
        font-weight: bold;
        color: white;
        opacity: 0.8;
    }
    
    .builder-content button:hover
    {
        opacity: 1;
        cursor: pointer;
    }

</style>