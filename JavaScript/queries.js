var jquery = document.createElement('script');
jquery.src = "http://code.jquery.com/jquery-latest.min.js";
document.getElementsByTagName("head")[0].appendChild(jquery);

const USER_KEY = "useridentity";
const EMPLOYEE_KEY = "employeeinfo";

function initUser(username, password)
{
    var userBackup;
    var settings = 
    {
        "async": false,
        "crossDomain": true,
        "url": "http://127.0.0.1:8000/API/v1/login/" + username + "/" + password,
        "method": "GET",
    };
    $.ajax(settings).done(function (response){
        localStorage.setItem(USER_KEY, JSON.stringify(response));

    });
    console.log(localStorage.getItem(USER_KEY));

    return USER_KEY;
}

function initManagerList()
{
    var settings = 
        {
            "async": false,
            "crossDomain": true,
            "url": "http://127.0.0.1:8000/API/v1/managers/",
            "method": "GET",
        };
        $.ajax(settings).done(function (response){
            localStorage.setItem('managerList', JSON.stringify(response));
        });

        return "managerList";
}

function initEmployeeInfo()
{
    var settings = 
    {
        "async": false,
        "crossDomain": true,
        "url": "http://127.0.0.1:8000/API/v1/employee/"+ getUserID().toString(),
        "method": "GET",
    };
     $.ajax(settings).done(function (response){
        localStorage.setItem(EMPLOYEE_KEY, JSON.stringify(response));
        console.log(JSON.parse(localStorage.getItem(EMPLOYEE_KEY)));
    });

    return EMPLOYEE_KEY;
}

function getUserID()
{
  if (localStorage.getItem('userid') != undefined && localStorage.getItem("userid") != null)
  {
      return localStorage.getItem("userid");
  }
  
  alert("Please ensure that a user is signed into the website before requesting a user id");
}

function isManager()
{
    if (localStorage.getItem("isManager") == null)
    {
        alert("We cannot determine if this user is a manager, please make sure that you are signed in");
    }
    else if(localStorage.getItem("isManager"))
    {
        return true;
    }
    
    return false;
}

function getCurrentUser()
{
    console.log(localStorage.getItem(USER_KEY));
    return JSON.parse(localStorage.getItem(USER_KEY));

}

function getEmployeeInfo()
{
    if (JSON.parse(localStorage.getItem(EMPLOYEE_KEY)) == undefined)
    {
        alert("Please sign in as an employee before requesting the employee info");
    }
    else
    {
        return JSON.parse(localStorage.getItem(EMPLOYEE_KEY));
    }
}