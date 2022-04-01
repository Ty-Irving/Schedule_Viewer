<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel = "stylesheet" href = "../CSS/styles.css"/>
    <title>Requests</title>
</head>
<body>
    <div class = "header">
        <a href = "../PHP/builder.php"><img class = "header-img" src = "https://cdn.iconscout.com/icon/free/png-256/timer-83-470366.png"></a>
        <div class = "header-info">
            <a class = "header-link" id = "header-link-1" href = "../PHP/departments.php">MANAGE DEPT</a>
            <a class = "header-link" id = "header-link-2" style = "background-color: rgba(0, 136, 107, 0.768)" href = "../PHP/requests.php">REQUESTS</a>
            <a class = "header-link" id = "header-link-3" href = "../PHP/builder.php">BUILDER</a>
            <a class = "header-link" id = "header-link-4" href = "../PHP/index.php">LOGOUT</a>
        </div>
    </div>

    <div class="requests">
        <div class="request-item">
            <div class = "request-content">
                <div class="table-header"><p>Message #</p></div>
                <div class="table-header grid-row-3"><p>User</p></div>
                <div class="table-header" style="grid-column: span 2"><p>Content</p></div>
            
        
                <div class="table-cell"><p>1</p></div>
                <div class="table-cell" style="grid-row: 4;"><p>Bobby bob</p></div>
                <div class="table-cell" style="grid-row: span 3; grid-column: span 2;"><p>I cant work on Sundays</p></div>
            
            </div>

            <button class="request-button">Request Denied</button>
            <button class="request-button">Schedule Changed</button>
            <button class="request-button">Next Request</button>
        </div> 
    </div>
</body>
</html>

<style type="text/css">
    .request-item {
        display: grid;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
        grid-template-columns: repeat(3, 1fr);
        gap: 2rem;
        padding: 3rem
  
    }

    .request-content {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-column: span 3;
        text-align: center;

    }

    .grid-row-2 {
        grid-row: 2;
    }

    .grid-row-3 {
        grid-row: 3;
    }

    .table-cell {
        border: 1.5px black solid;
        background-color: #3c454f;
        font-family: 'Source Sans Pro', sans-serif;
        /*border-bottom-left-radius: 5px;*/
        /*border-bottom-right-radius: 5px;*/
        color: white;
    }

    .table-header {
        background-color: rgba(0, 136, 107, 0.768);
        font-family: 'Source Sans Pro', sans-serif;
        font-weight: bold;
        border: 1.5px black solid;
        /*border-top-left-radius: 5px;*/
        /*border-top-right-radius: 5px;*/
    }

    .requests {
        padding-top: 15rem;
    }

    .request-button {
        background-color: #3c454f;
        border: none;
        padding: 1.2rem;
        margin-left: 1px;
        margin-right: 1px;
        color: white;
        font-family: 'Source Sans Pro', sans-serif;
        font-weight: bold;
        border-radius: 10px;
        cursor: pointer;
        border: black 1px solid;
    }

</style>