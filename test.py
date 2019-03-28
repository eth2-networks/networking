from networking.interfaces import Bridge, Loopback


br = Bridge.create('br-lan')
lo = Loopback.create('lo0')
