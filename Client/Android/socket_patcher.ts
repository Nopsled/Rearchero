
export class Patcher {


const getaddrinfoPtr = Module.findExportByName(null, 'getaddrinfo');
const connectPtr = Module.findExportByName(null, 'connect');
const sendPtr = Module.findExportByName(null, 'send');
const recvPtr = Module.findExportByName(null, 'recv');
const ntohsPtr = Module.findExportByName(null, 'ntohs');
const inet_addrPtr = Module.findExportByName(null, 'inet_addr');
if (getaddrinfoPtr != null && connectPtr != null && sendPtr != null && recvPtr != null && ntohsPtr != null && inet_addrPtr != null) {
    var getaddrinfoFunction = new NativeFunction(getaddrinfoPtr, 'int', ['pointer', 'pointer', 'pointer', 'pointer'])
    var connectFunction = new NativeFunction(connectPtr, 'int', ['int', 'pointer', 'int'])
    var sendFunction = new NativeFunction(sendPtr, 'int', ['int', 'pointer', 'int', 'int'])
    var recvFunction = new NativeFunction(recvPtr, 'int', ['int', 'pointer', 'int', 'int'])
    var ntohs = new NativeFunction(ntohsPtr, 'uint16', ['uint16']);
    var inet_addr = new NativeFunction(inet_addrPtr, 'int', ['pointer']);
    var connect = new NativeFunction(connectPtr, 'int', ['int', 'pointer', 'uint']);
}


/**
 * Returns hex from an ArrayBuffer object
 * @param {ArrayBuffer} array Array to work with
 * @param {Boolean} hex Whether to convert to hex or plain string
 */
function getReadable(array: any, hex: any) {
    var result = new Uint8Array(array.byteLength)
    result.set(array, 0)
    if (hex == false) {
        var str = ''
        for (var i = 0; i < result.length; i++) {
            str += String.fromCharCode(result[i])
        }
        return str
    }
    else {
        var hexStr = ''
        for (var i = 0; i < result.length; i++) {
            hexStr += result[i].toString(16)
        }
        return hexStr
    }
}
/**
 * Returns a nice formatting of a function with parameters
 * @param {string} functionName The name of the function to format
 * @param {string[]} params The function parameters as strings
 */
function formatFunction(functionName: any, params: any, retval: any) {
    var result = ''
    result += functionName
    result += '('
    for (var i = 0; i < params.length; i++) {
        if (i != 0) {
            result += ', '
        }
        result += params[i]
    }
    result += ')'
    if (retval) {
        result += ' -> '
        result += retval
    }
    return result
}
function replaceGadp() {
    if (getaddrinfoPtr != null) {
        Interceptor.replace(getaddrinfoPtr, new NativeCallback(function (name, service, req, pai) {
            const nameStr = name.readUtf8String()
            const newNamePtr = Memory.allocUtf8String("localhost")
            console.log(formatFunction('getaddrinfo', [nameStr, service, req, pai], ""))
            return getaddrinfoFunction(newNamePtr, service, req, pai)
        }, 'int', ['pointer', 'pointer', 'pointer', 'pointer']))
    }
}
function replaceConnect() {
    if (connectPtr != null) {
        Interceptor.replace(connectPtr, new NativeCallback(function (socket, address, addressLen) {
            var endpoint = {
                ip: '',
                port: 0
            }
            var ip = []
            const ipPtr = address.add(4)
            const portPtr = address.add(2)
            const port = ntohs(portPtr.readU16())
            endpoint.port = port

            if (port == 443) {
                ipPtr.writeInt(inet_addr(Memory.allocUtf8String("10.0.1.9")));
                console.log(formatFunction('connect', [socket, JSON.stringify(endpoint), addressLen], ""))
            }

            ip.push(ipPtr.add(0).readU8())
            ip.push(ipPtr.add(1).readU8())
            ip.push(ipPtr.add(2).readU8())
            ip.push(ipPtr.add(3).readU8())
            endpoint.ip = ip.join('.');

            var result = connectFunction(socket, address, addressLen)
            return result
        }, 'int', ['int', 'pointer', 'int']))
    }
}
function replaceSend() {
    if (sendPtr != null) {
        Interceptor.replace(sendPtr, new NativeCallback(function (fd, buf, len, flags) {
            var buffer = buf.readByteArray(len)
            var result = sendFunction(fd, buf, len, flags)
            console.log(formatFunction('send', [fd, getReadable(buffer, false), len, flags], result))
            return result
        }, 'int', ['int', 'pointer', 'int', 'int']))
    }
}
function replaceRecv() {
    if (recvPtr != null) {
        Interceptor.replace(recvPtr, new NativeCallback(function (fd, buf, len, flags) {
            var result = recvFunction(fd, buf, len, flags)
            if (result > -1) {
                var buffer = buf.readByteArray(result)
                console.log(formatFunction('recv', [fd, getReadable(buffer, false), len, flags], result))
            }
            else {
                console.log(formatFunction('recv', [fd, null, len, flags], result))
            }
            return result
        }, 'int', ['int', 'pointer', 'int', 'int']))
    }
}

}