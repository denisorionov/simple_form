function validateForm()  {
    var name = document.getElementById("userName").value;
    var surname = document.getElementById("userSurname").value;
    var gender = document.getElementsByName("gender");
    var date = document.getElementById("dateBorn").value;
    var education = document.getElementById("education").value;
    var str = /^[A-ZА-ЯЁ'][a-zа-яё']+$/;

    if (name == "") {
        alert("Пожалуйста, введите имя");
        return false;
                }

    if (! name.match(str)) {
        alert("Имя должно содержать только буквы и начинаться с заглавной буквы");
        return false
                }

    if (surname == "") {
        alert("Пожалуйста, введите фамилию");
        return false;
                }

    if (! surname.match(str)) {
        alert("Фамилия должна содержать только буквы и начинаться с заглавной буквы");
        return false
                }

    if ((gender[0].checked == false) && (gender[1].checked == false)){
        alert ( "Пожалуйста, выберите Ваш пол: Мужской или Женский" );
        return false;
                }

    if (date == "") {
        alert("Пожалуйста, укажите дату рождения");
        return false;
                }

    if (education == "") {
        alert("Пожалуйста, укажите ваше образование");
        return false;
                }


    alert("Данные успешно сохранены")
    return true;
    }