let counter = 0;
var room = document.getElementsByName('room');
for(i = 0; i < room.length; i++) {
    if(room[i].checked){
        counter+=1;
        break; 
    }
}
let price_dict = room[i].value;
let p_list = price_dict.split("_");
let price = Number(p_list[1]);



function priceAlter(){
    var room = document.getElementsByName('room');
    for(i = 0; i < room.length; i++) {
        if(room[i].checked){
            break; 
        }
    }
    let price_dict = room[i].value;
    let p_list = price_dict.split("_");
    price = Number(p_list[1]);
    CalculatePrice()
}


function Alterdate(){
    var input = document.getElementById('checkin_date').value;
    var now = new Date(input);
    // alert(now);
    var dt = now.getDate()+1;
    // alert(dt)
    var month = ("0" + (now.getMonth() + 1)).slice(-2);
    var year = now.getFullYear()
    var is_leap = leapYear(now.getFullYear());
    // alert(is_leap);
    if(is_leap==true){
        if(dt>29 && month==2){
            var dt = 1;
            var month = ("0" + (now.getMonth() + 2)).slice(-2);
        }
        else{
            if(month==1 || month==3 || month==5 || month==7 || month==8 || month==10){
                if(dt>31){
                    var dt = 1;
                    var month = ("0" + (now.getMonth() + 2)).slice(-2);
                }
            }
            if (month==4 || month==6 || month==9 || month==11){
                if(dt>30){
                    var dt = 1;
                    var month = ("0" + (now.getMonth() + 2)).slice(-2);
                }
            }
            if(month==12){
                if(dt>31){
                    var dt = 1;
                    var month = 01;
                    var year = year+1;
                }
            }
        }
    
        var day = ("0" + dt).slice(-2);
        var today = (month)+"/"+(day)+"/"+(year) ;
        $('#checkout_date').val(today);
    
    }
    else{
        if(dt>28 && month==2){
            var dt = 1;
            var month = ("0" + (now.getMonth() + 2)).slice(-2);
        }
        else{
            if(month==1 || month==3 || month==5 || month==7 || month==8 || month==10){
                if(dt>31){
                    var dt = 1;
                    var month = ("0" + (now.getMonth() + 2)).slice(-2);
                }
            }
            if (month==4 || month==6 || month==9 || month==11){
                if(dt>30){
                    var dt = 1;
                    var month = ("0" + (now.getMonth() + 2)).slice(-2);
                }
            }
            if(month==12){
                if(dt>31){
                    var dt = 1;
                    var month = 01;
                    var year = year+1;
                }
            }
        }
    
        var day = ("0" + dt).slice(-2);
        var today = (month)+"/"+(day)+"/"+(year) ;
        $('#checkout_date').val(today);
    }

}

function CalculatePrice(){
    let adult = Number(document.getElementById('adult').value);
    let kid = Number(document.getElementById('kid').value);

    let total = adult*(price)+kid*price;

    document.getElementById('amount_payable').value = total;
    document.getElementById('price_static').innerHTML = total;

    
}


function submitForm(){
    let checkin = document.getElementById('checkin_date').value;
    let checkout = document.getElementById('checkout_date').value;
    let adult = document.getElementById('adult').value;
    let kid = document.getElementById('kid').value;

    
    if(checkin==0){                 //if checkin is not set
        return false;
    }
    else if(counter==0){                 //if room not selected
        return false;
    }
    else if(kid==0 && adult==0){         //if kid and adult not selected
        return false;
    }
    else{
        return true;
    }

    
}



function leapYear(year){
    var result; 
    
    if (year%400==0){
      result = true
    }
    else if(year%100==0){
      result = false
    }
    else if(year%4==0){
      result= true
    }
    else{
      result= false
    }
    return result
 }