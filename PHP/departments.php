<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Departments</title>
    <link rel="stylesheet" href="../CSS/styles.css">
</head>
<body>
    <div class = "header">
        <a href = "../PHP/builder.php"><img class = "header-img" src = "https://cdn.iconscout.com/icon/free/png-256/timer-83-470366.png"></a>
        <div class = "header-info">
            <a class = "header-link" id = "header-link-1" href = "../PHP/departments.php" style = "background-color: rgba(0, 136, 107, 0.768)">MANAGE DEPT</a>
            <a class = "header-link" id = "header-link-2" href = "../PHP/requests.php">REQUESTS</a>
            <a class = "header-link" id = "header-link-3" href = "../PHP/builder.php">BUILDER</a>
            <a class = "header-link" id = "header-link-4" href = "../PHP/index.php">LOGOUT</a>
        </div>
    </div>

    <div class="content" style="padding: 1.5rem;">
        
        <button>add department</button>
        <br/>
        <div style="margin:1.5rem">
            <div class="department-element">
                <p>Name: Research</p>
                <p>ManagerID: 21</p>
                <a href="./deparment-view.php">VIEW</a>
                <a href="./department-builder.php">EDIT</a>
                <a href="departments.php">DELETE</a>
            </div>

            <div class="department-element">
                <p>Name: Finance</p>
                <p>ManagerID: 82</p>
                <a href="./deparment-view.php">VIEW</a>
            </div>
        </div>
    </div>
</body>
</html>

<style type="text/css">
    .content {
        background-color: #3c454f;
        margin-top: 15%;
    }

    .department-element {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        border: 2px black solid;
        padding: 5px;
        color: white;
        text-align: center;
    }

    a {
        text-decoration: none;
        color: white;
    }
</style>