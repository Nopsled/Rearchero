import "frida-il2cpp-bridge";
// sudo frida -l _.js "Archero" --runtime=v8

function log(message: string): void {
    console.log(message);
}

Il2Cpp.perform(() => {

    console.log("[AGENT]: Injected and rebuilt");
    
    const AssemblyCSharp = Il2Cpp.Domain.assembly("Assembly-CSharp").image;
    const AssemblyHabbyMail = Il2Cpp.Domain.assembly("HabbyMailLib").image;
    const AssemblyHabbyTool = Il2Cpp.Domain.assembly("HabbyToolLib").image;
    //const AssemblyUnityWebRequestModule = Il2Cpp.Domain.assembly("UnityEngine.UnityWebRequestModule").image;
    //const AssemblyLibA = Il2Cpp.Domain.assembly("lib").image;



    const HttpManager = AssemblyHabbyTool.class("Habby.Tool.Http.HttpManager");

    const HabbyClient = AssemblyCSharp.class("HabbyClient");


    // Classes with activity + interest
    const NetEnc = AssemblyCSharp.class("Habby.Archero.Crypto.NetEnc");
    const TGAnalytics = AssemblyCSharp.class("Habby.TGAnalytics");
    const PlayerPrefsEncrypt = AssemblyCSharp.class("PlayerPrefsEncrypt");
    const TcpNetManager = AssemblyCSharp.class("TcpNetManager");
    const NetEncrypt = AssemblyCSharp.class("NetEncrypt");
    const RC4Encrypter = AssemblyCSharp.class("RC4Encrypter");
    const SdkManager = AssemblyCSharp.class("SdkManager");
    const CUserLoginPacket = AssemblyCSharp.class("GameProtocol.CUserLoginPacket");

    // Habby.Mail system (all dumped)
    const HabbyMailEventDispatch = AssemblyHabbyMail.class("Habby.Mail.HabbyMailEventDispatch");
    const HabbyMailNoticeType = AssemblyHabbyMail.class("Habby.Mail.HabbyMailNoticeType");
    const MailHttpManager = AssemblyHabbyMail.class("Habby.Mail.MailHttpManager");
    const MailManager = AssemblyHabbyMail.class("Habby.Mail.MailManager");
    const MailRequestPath = AssemblyHabbyMail.class("Habby.Mail.MailRequestPath");
    const MailSetting = AssemblyHabbyMail.class("Habby.Mail.MailSetting");
    const StoreChannel = AssemblyHabbyMail.class("Habby.Mail.StoreChannel");

    //const CustomBinaryWriter = AssemblyCSharp.class("CustomBinaryWriter");

    // Not interesting classes
        // const Http = AssemblyCSharp.class("Habby.Archero.Network.Http");


    
    HttpManager.methods.forEach((method => {
        HttpManager.method(method.name).implementation = function (this: any, ...args: any[]) {
            log("[HttpManager::" + method.name + "]: " + args.toString());
            return this.method(method.name).invoke(...args);
        }
    }));

    
    
    
    


    // HabbyMailEventDispatch.methods.forEach((method => {
    //     HabbyMailEventDispatch.method(method.name).implementation = function (this: any, ...args: any[]) {
    //         log("[HabbyMailEventDispatch::" + method.name + "]: " + args.toString());
    //         return this.method(method.name).invoke(...args);
    //     }
    // }));
    // HabbyMailNoticeType.methods.forEach((method => {
    //     HabbyMailNoticeType.method(method.name).implementation = function (this: any, ...args: any[]) {
    //         log("[HabbyMailNoticeType::" + method.name + "]: " + args.toString());
    //         return this.method(method.name).invoke(...args);
    //     }
    // }));
    // MailHttpManager.methods.forEach((method => {
    //     MailHttpManager.method(method.name).implementation = function (this: any, ...args: any[]) {
    //         log("[MailHttpManager::" + method.name + "]: " + args.toString());
    //         return this.method(method.name).invoke(...args);
    //     }
    // }));
    // MailManager.methods.forEach((method => {
    //     MailManager.method(method.name).implementation = function (this: any, ...args: any[]) {
    //         log("[MailManager::" + method.name + "]: " + args.toString());
    //         return this.method(method.name).invoke(...args);
    //     }
    // }));
    // MailRequestPath.methods.forEach((method => {
    //     MailRequestPath.method(method.name).implementation = function (this: any, ...args: any[]) {
    //         log("[MailRequestPath::" + method.name + "]: " + args.toString());
    //         return this.method(method.name).invoke(...args);
    //     }
    // }));
    // MailSetting.methods.forEach((method => {
    //     MailSetting.method(method.name).implementation = function (this: any, ...args: any[]) {
    //         log("[MailSetting::" + method.name + "]: " + args.toString());
    //         return this.method(method.name).invoke(...args);
    //     }
    // }));





    HabbyClient.methods.forEach((method => {
        HabbyClient.method(method.name).implementation = function (this: any, ...args: any[]) {
            log("[HabbyClient::" + method.name + "]: " + args.toString());
            return this.method(method.name).invoke(...args);
        }
    }));




    // Classes with activity and interest
    // TGAnalytics.methods.forEach((method => {
    //     TGAnalytics.method(method.name).implementation = function (this: any, ...args: any[]) {
    //         log("[TGAnalytics::" + method.name + "]: " + args.toString());
    //         return this.method(method.name).invoke(...args);
    //     }
    // }));
    // PlayerPrefsEncrypt.methods.forEach((method => {
    //     PlayerPrefsEncrypt.method(method.name).implementation = function (this: any, ...args: any[]) {
    //         log("[PlayerPrefsEncrypt::" + method.name + "]: " + args.toString());
    //         return this.method(method.name).invoke(...args);
    //     }
    // }));
    // const TcpNetManagerIgnoreMethods = [
    //     ""
    // ]
    // TcpNetManager.methods.forEach((method => {
    //     if (TcpNetManagerIgnoreMethods.indexOf(method.name) > -1) return;
    //     TcpNetManager.method(method.name).implementation = function (this: any, ...args: any[]) {
    //         log("[TcpNetManager::" + method.name + "]: " + args.toString());
    //         return this.method(method.name).invoke(...args);
    //     }
    // }));
    // // const NetEncryptIngoreMethods = [
    // //     "Encrypt_Bytes"
    // // ]
    // // NetEncrypt.methods.forEach((method => {
    // //     if (NetEncryptIngoreMethods.indexOf(method.name) > -1) return;
    // //     NetEncrypt.method(method.name).implementation = function (this: any, ...args: any[]) {
    // //         log("[NetEncrypt::" + method.name + "]: " + args.toString());
    // //         return this.method(method.name).invoke(...args);
    // //     }
    // // }));
    // const SdkManagerIgnoreMethods = [
    //     "_isDebugMode",
    //     "_isTestServer"
    // ]
    // SdkManager.methods.forEach((method => {
    //     if (SdkManagerIgnoreMethods.indexOf(method.name) > -1) return;
    //     SdkManager.method(method.name).implementation = function (this: any, ...args: any[]) {
    //         log("[SdkManager::" + method.name + "]: " + args.toString());
    //         return this.method(method.name).invoke(...args);
    //     }
    // }));
    // const RC4EncrypterIngoreMethods = [
    //     "get_pwd",
    //     "Encrypt"
    // ]
    // RC4Encrypter.methods.forEach((method => {
    //     if (RC4EncrypterIngoreMethods.indexOf(method.name) > -1) return;
    //     RC4Encrypter.method(method.name).implementation = function (this: any, ...args: any[]) {
    //         log("[RC4Encrypter::" + method.name + "]: " + args.toString());
    //         return this.method(method.name).invoke(...args);
    //     }
    // }));
    // CUserLoginPacket.methods.forEach((method => {
    //     CUserLoginPacket.method(method.name).implementation = function (this: any, ...args: any[]) {
    //         log("[CUserLoginPacket::" + method.name + "]: " + args.toString());
    //         return this.method(method.name).invoke(...args);
    //     }
    // }));




    // Classes with no activity
    const SocketObject = AssemblyCSharp.class("NetWork.SocketObject");
    const Crypto = AssemblyCSharp.class("crypto.Security");

    // Nothing found in these classes
    SocketObject.methods.forEach((method => {
        SocketObject.method(method.name).implementation = function (this: any, ...args: any[]) {
            log("[SocketObject::" + method.name + "]: " + args.toString());
            return this.method(method.name).invoke(...args);
        }
    }));
    Crypto.methods.forEach((method => {
        Crypto.method(method.name).implementation = function (this: any, ...args: any[]) {
            log("[Crypto::" + method.name + "]: " + args.toString());
            return this.method(method.name).invoke(...args);
        }
    }));
    NetEnc.methods.forEach((method => {
        NetEnc.method(method.name).implementation = function (this: any, ...args: any[]) {
            log("[NetEnc::" + method.name + "]: " + args.toString());
            return this.method(method.name).invoke(...args);
        }
    }));



    const SSLFunctions = [
        // "SSL_read",
        // "SSL_write",
        // "SSL_do_handshake",
        // "SSL_is_dtls",
        // "SSL_get_session",
         "SSL_in_init",
        // "SSL_SESSION_dup",
        // "SSL_SESSION_free",
        // "SSL_get_ex_data",
        // "SSL_SESSION_free",
        // "SSL_get1_session",
        // "SSL_in_init",
        // "SSL_get_certificate",
        // "SSL_get_peer_full_cert_chain",
        // "SSL_CTX_set_cert_verify_callback"
    ]

    Process
        .getModuleByName('libboringssl.dylib')
        .enumerateExports().filter(exp => exp.type === 'function' && SSLFunctions.some(prefix => exp.name.indexOf(prefix) === 0))
        .forEach(exp => {
            Interceptor.attach(exp.address, {
                onEnter: function (args) {

                    this.exp = exp
                    //console.log("Function hooked: " + exp.name)
                    if (exp.name == "SSL_CTX_set_cert_verify_callback") {
                        console.log("[SSL_CTX_set_cert_verify_callback] has been patched. args[0]: " + args[0])
                        args[1] = ptr("0x00")
                    }
                    //console.log("Function h00ked: " + exp.name)
                },
                onLeave: function (retval) {
                    console.log(JSON.stringify(this.exp) + " -  returned: " + retval.toInt32())
                }
            });
        });

    
    
    const SocketFunctions = [
        //'connect',
        'recv',
        // 'send',
        // 'read',
        // 'write'
    ]

    // Process
    //     .getModuleByName('libSystem.B.dylib')
    //     .enumerateExports().filter(exp => exp.type === 'function' && SocketFunctions.some(prefix => exp.name.indexOf(prefix) === 0))
    //     .forEach(exp => {
    //         Interceptor.attach(exp.address, {
    //             onEnter: function (args) {
    //                 var fd = args[0].toInt32();
    //                 var socktype = Socket.type(fd);
    //                 var data = args[1]
    //                 var size = args[2].toInt32();
                    
    //                 if (socktype !== 'tcp' && socktype !== 'tcp6')
    //                     return;
    //                 var address = Socket.peerAddress(fd);
    //                 if (address === null)
    //                     return;
                    
    //                 // var data = args[1]
    //                 // var size = args[2].toInt32();
    //                 var buffer = data.readByteArray(size);
    //                 console.log(exp.name + "("+fd+")"+ JSON.stringify(address) + " – " + size + " bytes (" + socktype + ")");
    //                 // if (buffer != null)
    //                 //     console.log(hexdump(buffer, { offset: 0, length: 800, header: false, ansi: true }));
  
    //             },
    //             onLeave: function (retval) {
    //             }
    //         })
    //     })


    // if (connect != null)
    //     Interceptor.attach(connect, {
    //         onEnter: function (args) {

    //             this.sockFd = args[0].toInt32()

    //             // var portLoc = args[1].add(2);
    //             // var ipLoc = args[1].add(4);
    //             // var port = ntohs(portLoc.readU16());

    //             // log("[Socket::Connect]: " + port);
    //             // // port === 9952 || 8080 || port === 443
    //             // if (port == 9952 || port == 8080 || port == 443) { 

    //             //     var fd = args[0].toInt32();
    //             //     var socktype = Socket.type(fd);
    //             //     var host = inet_addr(Memory.allocUtf8String("10.0.1.9"))
    //             //     var ip = ntohs(ipLoc.readU16());
        
    //             //     ipLoc.writeInt(host);
    //             //     log("[Redirecting – Socket::Connect]: " + port);

    //             // }
    //         },
    //         onLeave: function (retval) {
    //             // const sockFd = this.sockFd
    //             // const sockType = Socket.type(sockFd)
    //             // const port = ntohs(portLoc.readU16());

    //             // if (!(sockType === "tcp6" || sockType === "tcp")) return

    //             // const sockLocal = Socket.localAddress(sockFd)
    //             // const sockRemote = Socket.peerAddress(sockFd)
    //             // if (sockRemote === null) return

    //             // log("[Socket::Connect (onLeave)]: " + port);

    //         }
    //     });

});