$(document).ready(function () {
    
   
    $("#reg").click(function (e) { 
        e.preventDefault();
        $("#regload").load("register");
    });
    $("#reghere").click(function (e) { 
        e.preventDefault();
        $("#regload").load("register");
    
    });
    $("#preg").click(function (e) { 
        e.preventDefault();
        $("#pload").load("patients_register");
    
    });
    
    $("#dforget").click(function (e) { 
        e.preventDefault();
        $("#regload").load("Doctor_forgot");
        
    });
    
    $("#pforget").click(function (e) { 
        e.preventDefault();
        $("#pload").load("patients_forget");
    
    });
    
});

