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

function decode(text, key){
    return simplify_des(atob(text), key)
}

// console.log(decode("HQoUVB0GA1UITFRER1pfBEVVVU1dWlY=", "section02lesson1"))