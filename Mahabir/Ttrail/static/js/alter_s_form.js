function Alter_date(){
    var input = document.getElementById('checkin_dates').value;
    var now = new Date(input);
    var dt = now.getDate()+1;
    var month = ("0" + (now.getMonth() + 1)).slice(-2);
    var year = now.getFullYear()
    var is_leap = leapYear(now.getFullYear());
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
        $('#checkout_dates').val(today);
    
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





function leapYear(year){
    var result; 
    
    if (year/400){
      result = true
    }
    else if(year/100){
      result = false
    }
    else if(year/4){
      result= true
    }
    else{
      result= false
    }
    return result
 }