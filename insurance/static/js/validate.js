
const age = document.getElementById("age");
const bmi=document.getElementById("bmi");
const children=document.getElementById("children");

const form=document.getElementById("data-form");

const green='#4CAF50';
const red='#F44336';

function validateAge(){
    if(checkEmpty(age)){
        return true;
    }else{
        return false;
    }
}

function checkEmpty(field){
    if(isEmpty(field.value.trim())){
        setInvalid(field, `${field.name} must not be empty`)
        return true;
    }
}

function isEmpty(value){
    if(value === ''){
        return true;
    }else{
        false;
    }
}