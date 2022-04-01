<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel = "stylesheet" href = "../CSS/styles.css"/>
    <title>Schedule Viewer</title>
</head>
<body>
    <div class = "header">
        <a href = "../PHP/schedule_view.php"><img class = "header-img" src = "https://cdn.iconscout.com/icon/free/png-256/timer-83-470366.png"></a>
        <div class = "header-info">
            <a class = "header-link" href="../PHP/update.php"> UPDATE INFO</a>
            <a class = "header-link" style = "background-color: rgba(0, 136, 107, 0.768)" href = "../PHP/schedule_view.php">SCHEDULE VIEW</a>
            <a class = "header-link" href = "../PHP/index.php">LOGOUT</a>
        </div>
    </div>

    <div class = "content-box">
        <img src = "../PHP/request.png" class = "request-img" onclick="showRequestPrompt()" id="request_img">
        
        <div class = "request-box" id="request_box">
            <p class = "request-box-header">Make Request</p>
            <input type="text" placeholder = "Type employee ID...">
            <textarea id="" cols="20" rows="8" placeholder="Type request..."></textarea>
            <button class = "btn"></script>SUBMIT</button>
            <button class = "btn cancel" onclick="hideRequestPrompt()">CLOSE</button>
        </div>

        <div class = "schedule-view">
            <div>
                <table class = "hours">
                    <tr style="background-color: rgba(0, 136, 107, 0.768); color: white;" >
                        <th></th>
                        <th>S</th>
                        <th>M</th>
                        <th>T</th>
                        <th>W</th>
                        <th>T</th>
                        <th>F</th>
                        <th>S</th>
                    </tr>
                    <tr class="light-table-row">
                        <th>8:00AM</th><th></th><th></th><th></th><th></th><th></th><th></th><th></th>
                    </tr>
                    <tr class="dark-table-row">
                        <th>9:00AM</th><th></th><th></th><th></th><th></th><th></th><th></th><th></th>
                    </tr>
                    <tr class="light-table-row">
                        <th>10:00AM</th><th></th><th></th><th></th><th></th><th></th><th></th><th></th>
                    </tr>
                    <tr class="dark-table-row">
                        <th>11:00AM</th><th></th><th></th><th></th><th></th><th></th><th></th><th></th>
                    </tr>
                    <tr class="light-table-row">
                        <th>12:00AM</th><th></th><th></th><th></th><th></th><th></th><th></th><th></th>
                    </tr>
                    <tr class="dark-table-row">
                        <th>1:00PM</th><th></th><th></th><th></th><th></th><th></th><th></th><th></th>
                    </tr>
                    <tr class="light-table-row"> 
                        <th>2:00PM</th><th></th><th></th><th></th><th></th><th></th><th></th><th></th>
                    </tr>
                    <tr class="dark-table-row">
                        <th>3:00PM</th><th></th><th></th><th></th><th></th><th></th><th></th><th></th>
                    </tr>
                    <tr class="light-table-row">
                        <th>4:00PM</th><th></th><th></th><th></th><th></th><th></th><th></th><th></th>
                    </tr>
                    <tr class="dark-table-row">
                        <th>5:00PM</th><th></th><th></th><th></th><th></th><th></th><th></th><th></th>
                    </tr>
                    <tr class="light-table-row">
                        <th>6:00PM</th><th></th><th></th><th></th><th></th><th></th><th></th><th></th>
                    </tr>
                    
                    
                </table>
            </div>
        </div>
        <div class = "invoice-view">
            <div class = "invoice-content">
                <div class = "user-header">
                    User ABC Expected Pay
                </div>
                <div class = user-invoice>
                    <ul>
                        <li class = "invoice-list">User Name: Jerry</li>
                        <li class = "invoice-list">User ID: 12332</li>
                        <li class = "invoice-list">Hours worked: 50</li>
                        <li class = "invoice-list">Hourly Salary: $5.00</li>
                    </ul>
                </div>
                <div class = "expected-pay">
                    Total Pay: $24000.00
                </div>
            </div>
        </div>
    </div>
</body>
</html>

<script type="text/javascript">
    const REQUEST_PROMPT = document.getElementById("request_box");
    const REQUEST_IMG = document.getElementById("request_img");

    function hideRequestPrompt()
    {
        REQUEST_PROMPT.style.display='none';
        showRequestImg();
    }

    function showRequestPrompt()
    {
        REQUEST_PROMPT.style.display="inline";
        hideRequestImg();
    }

    function hideRequestImg()
    {
        REQUEST_IMG.style.display="none";
    }

    function showRequestImg()
    {
        REQUEST_IMG.style.display="inline";
    }
</script>

<style type="text/css">
    
    .request-img {
        width: 65px;
        height: 65px;
        bottom: 0;
        right: 0;
        margin: 10px;
        position: fixed;
        filter: invert();
    }

    .request-img:hover {
        cursor: pointer;
    }

    .request-box textarea {
        margin-left: 15px;
        margin-top: 10px;
        resize: none;
        width: 88%;
        min-height: 200px;
        margin-bottom: 10px;
    }
    
    .request-box-header {
        margin-left: 15px;
        font-size: 25px;
        margin-bottom: 5px;
        margin-top: 10px;
    }
    
    .request-box input {
        width: 87%;
        margin-left: 15px;
    }
    
    .request-box {
        border: black 1px;
        bottom: 0;
        right: 0;
        position: fixed;
        margin-right: 15px;
        margin-bottom: 15px;
        height: 400px;
        max-width: 300px;
        background-color: #3c454f;
        color: white;
        font-weight: bold;
        display: none;
    }
    
    .request-box .btn {
        background-color: #04AA6D;
        color: white;
        padding: 10px 20px;
        margin-left: 15px;
        border: none;
        cursor: pointer;
        width: 90%;
        margin-bottom: 10px;
        opacity: 0.8;
    }
    
    .request-box .btn:hover {
        opacity: 1;
    }
    
    .request-box .cancel {
        background-color: red;
    }

    .invoice-view {
        background-color: #3c454f;
        width: 300px;
        height: 400px;
        margin: 50px;
        display: inline-block;
        border: 2px black solid;
        color: white;
    }

    .schedule-view {
        background-color: #3c454f;
        width: 600px;
        height: 400px;
        margin: 50px;
        /*margin-left: 10%;*/
        display: inline-block;
        border: 2px black solid;
        /*border-radius: 5%;*/
        grid-column: 2;

        
    }


    .invoice-list {   
        
        margin-top: 30px;
        list-style: none;
        list-style-type: none;
        padding: 0;
    }

    .expected-pay {
        font-size: 20px;
        margin-left: auto;
        margin-right: auto;
        text-align: center;
        margin-top: 20%;
        font-weight: bold;
    }

    .hours {
        margin: 2.5rem auto;
        background-color: #3c454f;
    }

    .content-box {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        padding-top: 5rem;
    }

    .light-table-row {
        background-color: #829CBC;
    }

    .dark-table-row {
        background-color: #73879F;
    }



</style>