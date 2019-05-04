// $(document).on ('submit','#doctorprofile',function(e){
//     e.preventDefault();
//     $.ajax({
//         type:'POST',
//         url:'/dashboard/settings',
//         data:
//         {
//             first_name=$("#id_first_name"),
//             last_name=$("#id_last_name"),
//             email=$("#id_email"),
//             address=$("#id_address"),
//             speciality=$("id_speciality"),
//             degree=$("#id_degree"),
//             gender=$("#id_gender"),
//             experience=$("id_Experience"),
//             fees=$("#id_fees"),
//         },
//         sucess:function()
//         {
            
//         }
//     });
// });

$(document).ready(function () {
    $("#submit").click(function (e) { 
        e.preventDefault();
        setInterval(function(){
            $("#changepassword").load().fadein("slow");
        },1000);        
    });
});
