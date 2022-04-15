var jquery = document.createElement('script');
jquery.src = "http://code.jquery.com/jquery-latest.min.js";
document.getElementsByTagName("head")[0].appendChild(jquery);

// LOCAL STORAGE RETRIEVAL KEYS -------------------------------------------------------------------------------------------------------------------------------

const USER_KEY = "useridentity";
const USER_LIST_KEY = "users-department";
const EMPLOYEE_KEY = "employeeinfo";
const EMPLOYEE_LIST_KEY = "employee_list";
const MANAGER_KEY = "manageridentity";
const MANAGER_LIST_KEY = "Managers";
const DEPARTMENT_LIST_KEY = "Departments";
const REQUEST_LIST_KEY = "requests";

// INITIALIZATION  QUERIES ------------------------------------------------------------------------------------------------------------------------------------

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

function initUserList()
{
    var settings = 
    {
        "async": false,
        "crossDomain": true,
        "url": "http://127.0.0.1:8000/API/v1/users/",
        "method": "GET",
    };
     $.ajax(settings).done(function (response){
        localStorage.setItem(USER_LIST_KEY, JSON.stringify(response));
        console.log(localStorage.getItem(USER_LIST_KEY));
    });

    return USER_LIST_KEY;
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

function initManagerInfo()
{
    settings = 
    {
        "async": false,
        "crossDomain": true,
        "url": "http://127.0.0.1:8000/API/v1/managers/" + getUserID(),
        "method": "GET",
    };
     $.ajax(settings).done(function (response){
        localStorage.setItem(MANAGER_KEY, JSON.stringify(response));
        console.log(localStorage.getItem(MANAGER_KEY));
    });

    return MANAGER_KEY;
}

function initEmployeeList()
{
    var settings = 
    {
        "async": false,
        "crossDomain": true,
        "url": "http://127.0.0.1:8000/API/v1/employee/",
        "method": "GET",
    };
     $.ajax(settings).done(function (response){
        localStorage.setItem(EMPLOYEE_LIST_KEY, JSON.stringify(response));
        console.log(localStorage.getItem(EMPLOYEE_LIST_KEY));
    });

    return MANAGER_LIST_KEY;
}

function initiManagerList()
{
    // $("#manager-id").empty();
    var settings = 
    {
        "async": false,
        "crossDomain": true,
        "url": "http://127.0.0.1:8000/API/v1/managers/",
        "method": "GET",
    };
     $.ajax(settings).done(function (response){
        localStorage.setItem(MANAGER_LIST_KEY, JSON.stringify(response));
        console.log(localStorage.getItem(MANAGER_LIST_KEY));
    });

    return EMPLOYEE_LIST_KEY;
}

function initDepartmentList()
{
    var settings = 
    {
        "async": false,
        "crossDomain": true,
        "url": "http://127.0.0.1:8000/API/v1/departments/",
        "method": "GET",
    };
     $.ajax(settings).done(function (response){
        localStorage.setItem(DEPARTMENT_LIST_KEY, JSON.stringify(response));
        console.log(localStorage.getItem(DEPARTMENT_LIST_KEY));
    });

    return DEPARTMENT_LIST_KEY;
}

function initRequestList()
{
    var settings = 
    {
        "async": false,
        "crossDomain": true,
        "url": "http://127.0.0.1:8000/API/v1/requests/",
        "method": "GET",
    };
    $.ajax(settings).done(function (response){
        localStorage.setItem(REQUEST_LIST_KEY, JSON.stringify(response));
        console.log(localStorage.getItem(REQUEST_LIST_KEY));
    });
    requests = JSON.parse(localStorage.getItem('requests'))
}

// GETTERS ---------------------------------------------------------------------------------------------------------------------------------------------------------

function getUserID()
{
  if (localStorage.getItem('userid') != undefined && localStorage.getItem("userid") != null)
  {
      return localStorage.getItem("userid");
  }
  
  alert("Please ensure that a user is signed into the website before requesting a user id");
}

function getManagerID()
{
    if (JSON.parse(localStorage.getItem(MANAGER_KEY)) == undefined)
    {
        alert("This user does not appear to be a manager");
    }
    else
    {
        return JSON.parse(localStorage.getItem(MANAGER_KEY)).id;
    }
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
        alert("This user is not an employee, please sign in as an employee before requesting the employee info");
    }
    else
    {
        return JSON.parse(localStorage.getItem(EMPLOYEE_KEY));
    }
}

function getManagerList()
{
    if (JSON.parse(localStorage.getItem(MANAGER_LIST_KEY)) == undefined)
    {
        alert("There are no managers");
    }
    else
    {
        return JSON.parse(localStorage.getItem(MANAGER_LIST_KEY));
    }
}

function getDepartmentList()
{
    if (JSON.parse(localStorage.getItem(DEPARTMENT_LIST_KEY)) == undefined)
    {
        alert("There are no departments");
    }
    else
    {
        return JSON.parse(localStorage.getItem(DEPARTMENT_LIST_KEY));
    }
}

function getUserList()
{
    if (JSON.parse(localStorage.getItem(USER_LIST_KEY)) == undefined)
    {
        alert("unable to retrieve user list");
    }
    else
    {
        return JSON.parse(localStorage.getItem(USER_LIST_KEY));
    }
}

// UTILITY FUNCTIONS ----------------------------------------------------------------------------------------------------------------------------------------------

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

function isEmployee()
{
    var isemp = false;
    initEmployeeList();
    var empList = JSON.parse(localStorage.getItem(EMPLOYEE_LIST_KEY));

    empList.forEach(element => {
        if (getUserID() == element.EmpID)
        {
            isemp = true;
        }
    });

    return isemp;

}


