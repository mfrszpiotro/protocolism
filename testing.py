from entity import Entity, Packet, Simulation, createTimestamp

def test_handshake():
    pass

def test_2entity_communication():
    # Example of message sending
    e1 = Entity(1)
    e2 = Entity(2)
    
    simulation = Simulation()
    
    simulation.addEntity(e1)
    simulation.addEntity(e2)
    
    p1 = Packet(1, 2, "there is no try")
    simulation.sendMessage(p1)
    
    p2 = Packet(2, 1, "do or do not")
    simulation.sendMessage(p2)
    
    p3 = Packet(2, 1, "or have a donut")
    simulation.sendMessage(p3)
    
    p4 = Packet(2, 1, "or be gone")
    simulation.sendMessage(p4)
    
    # Exemplary listen message
    simulation.listenMessage(e1)
    
    return simulation

def test_3entity_communication():
    # Example of message sending
    e1 = Entity(1)
    e2 = Entity(2)
    e3 = Entity(3)
    
    simulation = Simulation()

    logfile = createTimestamp()
    print(logfile)
    
    simulation.addEntity(e1)
    simulation.addEntity(e2)
    simulation.addEntity(e3)
    
    p1 = Packet(1, 2, "one to two")
    simulation.sendMessage(p1, logfile)
    
    p1 = Packet(2, 3, "two to three")
    simulation.sendMessage(p1, logfile)

    p1 = Packet(3, 1, "three to one")
    simulation.sendMessage(p1, logfile)

    p1 = Packet(2, 1, "two to one")
    simulation.sendMessage(p1, logfile)

    p1 = Packet(3, 2, "three to two")
    simulation.sendMessage(p1, logfile)

    p1 = Packet(1, 3, "one to three")
    simulation.sendMessage(p1, logfile)
    
    # Exemplary listen message
    simulation.listenMessage(e1, logfile)
    simulation.listenMessage(e2, logfile)
    simulation.listenMessage(e3, logfile)
    
    return simulation