$(document).ready(function(){
    $('.buttons').click(function(){
        $(this).addClass('active').siblings().removeClass('active');

    var filter = $(this).attr('data-filter');

    if(filter == "all"){
        $('.image').show();
    }else{
        $('.image').not('.'+filter).hide(400);
        $('.image').filter('.'+filter).show(600);
    }

    });

    $('.gallery').magnificPopup({
        delegate:'a',
        type:'image',
        gallery:{
            enabled:true
        }
    })
});