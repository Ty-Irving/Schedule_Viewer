var jquery = document.createElement('script');
jquery.src = "http://code.jquery.com/jquery-latest.min.js";
document.getElementsByTagName("head")[0].appendChild(jquery);

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
        localStorage.setItem('useridentity', JSON.stringify(response));

    });
    console.log(localStorage.getItem("useridentity"));

    return "useridentity";
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