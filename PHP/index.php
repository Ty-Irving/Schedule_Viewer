<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel = "stylesheet" href = "../CSS/styles.css"/>
    <title>Log In</title>
</head>

<body class="bg">

    <div class = "login-panel">
        <div class = "login-header">
            Login
        </div>
        <div class = "input-box">
            <img src = "../PHP/user-img.png" class = "box-img">
            <input type = "text" class = "user-text" maxlength = "30" placeholder = "Username"></input>
        </div>
        <div class = "input-box">
            <img src = "../PHP/password-img.png" class = "box-img">
            <input type = "password" class = "user-text" maxlength = "30" placeholder = "Password"></input>
        </div>
        <div class = "create-acc">
            <a href = "create_account.php">Create Account</a>
        </div>
        <button class = "login-button">LOGIN</button>
        <a href = "builder.php">Admin part</a>
        <a href = "schedule_view.php">User content</a>
    </div>
</body>
</html>





<style type="text/css">

    .user-text {
        resize: none;
        display: block;
        margin-left: auto;
        margin-right: auto;
        width:  230px;
        height: 30px;
        float: right;
        border: none;
        outline: none;
        background-color: whitesmoke;
    }

    .create-acc
    {
        width: 40%;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 10px;
        margin-top: 5px;
        text-align: right;
        font-size: 14px;
        
    }

    a
    {
        color: #04AA6D;
    }


    .login-header
    {
        width: 40%;
        margin-left: auto;
        margin-right: auto;
        font-size: 24px;
        color: #04AA6D;
        font-weight: bold;
        padding-top: 90px;
    }

    .box-img
    {
        width: 25px;
        padding-left: 10px;
        padding-top: 3px;
    }

    .input-box
    {
        margin-top: 25px;
        width: 40%;
        margin-left: auto;
        margin-right: auto;
        border: rgb(49, 46, 46) 1px solid;
        height: 32px;
    }

    .login-button {
        margin-left: auto;
        margin-right: auto;
        display: block;
        width: 40%;
        margin-top: 5%;
        height: 40px;
        border-radius: 8px;
        border-style: double;
        background-color: #04AA6D;
        color: white; 
    }
    
    .login-panel {
        opacity: 88%;
        width: 700px;
        height: 60ex;
        background-color: whitesmoke;
        margin-left: auto;
        margin-right: auto;
        margin-top: 15%;
    }

    .bg {
        position: fixed;
        width: 100%;
        height: 100%;
        background: url("https://bit.ly/3tFgT8c");
        background-position: center;
        background-attachment: fixed;
        background-size: cover;
    }

    /* img
    {
        filter: invert(1);
    } */


</style>