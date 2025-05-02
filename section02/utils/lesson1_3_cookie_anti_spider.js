<script>
    function stringToBinary(input) {
    let binaryResult = "";
    for (let i = 0; i < input.length; i++) {
    let binaryChar = input.charCodeAt(i).toString(2);
    binaryResult += ("00000000" + binaryChar).slice(-8);
}
    console.log("stringToBinary", input, binaryResult)
    return binaryResult;
}

    function binaryToString(input) {
    let str = '';
    for (let i = 0; i < input.length; i += 8) {
    let byte = input.slice(i, i + 8);
    str += String.fromCharCode(parseInt(byte, 2));
}
    console.log("binaryToString", input, str)
    return str;
}

    function simpleEncryptDecrypt(inputBinary, keyBinary) {
    let result = '';
    for (let i = 0; i < inputBinary.length; i++) {
    result += inputBinary[i] === keyBinary[i % keyBinary.length] ? '0' : '1';
}
    console.log("simpleEncryptDecrypt", inputBinary, keyBinary)
    return result;
}

    function simplify_des(input, key) {
    let inputBinary = stringToBinary(input);
    let keyBinary = stringToBinary(key);
    // 加密或解密
    let encryptedBinary = simpleEncryptDecrypt(inputBinary, keyBinary);
    // 将二进制结果转换回字符串
    let result = binaryToString(encryptedBinary);
    console.log("simplify_des", input, key, result)
    return result;
}

    let text = "now time: " + getServerTime();
    let key = "section02lesson1";
    document.cookie = "token=" + btoa(simplify_des(text, key)) + ";path=/"; // cookie对于异常字符的传值并不友好，所以用base64进行一下编码为常见字符

</script>
