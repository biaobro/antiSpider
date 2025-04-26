function getServerTime(){
    let time_xml = new XMLHttpRequest()
    time_xml.open("get", "/section02/lesson1_server_time", false)
    time_xml.send()
    return parseInt(time_xml.responseText)
}