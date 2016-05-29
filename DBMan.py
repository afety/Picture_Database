from Database import DBSession,Brain,Abdomen,Iris,Lung_CR,Lung_CT

def insertBrain(local_addr,net_addr):
    session = DBSession()
    heading = Brain(local_addr=local_addr, net_addr=net_addr)
    session.add(heading)
    session.commit()
    session.close()

def insertLung_CT(local_addr,net_addr):
    session = DBSession()
    lung = Lung_CT(local_addr=local_addr, net_addr=net_addr)
    session.add(lung)
    session.commit()
    session.close()

def insertLung_CR(local_addr,net_addr):
    session = DBSession()
    lung = Lung_CR(local_addr=local_addr, net_addr=net_addr)
    session.add(lung)
    session.commit()
    session.close()

def insertIris(local_addr,net_addr):
    session = DBSession()
    pupil = Iris(local_addr=local_addr, net_addr=net_addr)
    session.add(pupil)
    session.commit()
    session.close()

def insertAbdomen(local_addr, net_addr):
    session = DBSession()
    abdomen = Abdomen(local_addr=local_addr, net_addr=net_addr)
    session.add(abdomen)
    session.commit()
    session.close()