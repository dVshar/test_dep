
$( document ).ready(function() {
    var date = new Date();
    var dt = date.getDate();
    var day = ("0" + dt).slice(-2);
    var month = ("0" + (date.getMonth() + 1)).slice(-2);
    var year = date.getFullYear();
    var today = (year)+'-'+(month)+"-"+(day);
    $('#checkin_date').attr('min' , today);
});


function stop_prev(){
    var reg_date = document.getElementById('checkin_date').value;
    var date = new Date(reg_date);
    var dt = date.getDate();
    var day = ("0" + dt).slice(-2);
    var month = ("0" + (date.getMonth() + 1)).slice(-2);
    var year = date.getFullYear();
    var today = (year)+'-'+(month)+"-"+(day);
    $( document ).ready(function() {
        $('#checkout_date').attr('min' , today);
});
}