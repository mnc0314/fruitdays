$(function () {
    // 为表单绑定提交事件
    $('#formReg').submit(function () {
        // 判断密码和重复密码是否相等
        if ($('#i2').val() != $('#i3').val()) {
            alert('两次密码输入不一致');
            return false;
        }
        return true;
    });
    $('#i1').bind('blur', function () {
        if ($('#i1').val().length != 11) {
            alert('手机号格式错误')
        }
    })
});