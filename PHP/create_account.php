<!DOCTYPE html>


<html>
<head>
	<meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel = "stylesheet" href = "../CSS/styles.css"/>
    <title>Create Account</title>
</head>


<body class = "background">
    
    <div class = "info-panel">
        <a href = "index.php"><button class = "cancel">X</button></a>
        <h1 class = "hdr">REGISTER</h1>
        <h3 class = "hdr-2">Personal Information</h3>
        <p>Name</p>
        <div class = "name-div">
            <input class = "name" placeholder = "First"></input>
            <input class = "name" placeholder = "Last"></input>
        </div>
        <p>Address</p>
        <input id = "location"></input>
        <h3 class = "hdr-2">Login Information</h3>
        <p>Username</p>
        <input id = "user"></input>
        <p>Password</p>
        <input id = "pwd" type = 'password'></input>
        <p>Confirm Password</p>
        <input id = "pwd-confirm" type = 'password'></input>
        <button class = "create">Create Account</button>
    </div>

</body>


</html>


<style type="text/css">

    .background {
        position: fixed;
        width: 100%;
        height: 100%;
        background-image: url('https://bit.ly/3IMzAeD');
    }

    .info-panel {
        opacity: 90%;
        width: 600px;
        height: 100ex;
        background-color: whitesmoke;
        margin-left: auto;
        margin-right: auto;
        margin-top: 5%;
        text-align: center;
        font-family: Verdana;
        font-size: small;
    }

    input {
        width: 40%;
        height: 3%;
        /* margin-left: 100px;
        margin-right: auto; */
    }

    .cancel {
        font-size: 130%;
        width: 5%;
        margin-left: 95%;
        border-width: 0px;
        background-color: whitesmoke;
    }

    .cancel:hover {
        background-color: red;
    }

    .name-div {
        height: 3%;
    }

    .name {
        width: 20%;
        text-align: center;
        height: 100%
    }

    .create {
        margin-left: auto;
        margin-right: auto;
        display: block;
        width: 40%;
        margin-top: 10%;
        height: 40px;
        border-radius: 8px;
        border-style: double;
        background-color: #04AA6D;
        color: white; 
    }


    .hdr {
        margin-left: 30%;
        text-align: center;
        color: black;
        width: 40%;
        border-top: 3px solid #04AA6D;
        border-bottom: 3px solid #04AA6D;
        border-radius: 10%;
        margin-bottom: 5%;
    }

    .hdr-2 {
        color: black;
        margin-top: 10%;
    }

    

    /* .deco {
        opacity: 40%;
        margin-left: 25%;
        margin-right: auto;
        margin-top: 5%;
        position: absolute;
    }

    .c-deco {
        width: 5%;
        height: 5%;
        background-color: red;
        position: fixed;
    } */

</style>





<script type="text/javascript">

    // if pwd-check == pwd:
    //     send it to API to be hashed and stored
    // else:
    //     do not send, set red outline on pwd-check box
    // function check_pass() {

    // }


</script>