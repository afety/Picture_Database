from Database import DBSession,Heading,Abdomen,Pupil,Lung

def insertHeading(local_addr,net_addr):
    session = DBSession()
    heading = Heading(local_addr,net_addr)
    session.add(heading)
    session.commit()
    session.close()

def insertLung(local_addr,net_addr):
    session = DBSession()
    lung = Lung(local_addr,net_addr)
    session.add(lung)
    session.commit()
    session.close()

def insertPupil(local_addr,net_addr):
    session = DBSession()
    pupil = Pupil(local_addr,net_addr)
    session.add(pupil)
    session.commit()
    session.close()

def insertAbdomen(local_addr,net_addr):
    session = DBSession()
    abdomen = Abdomen(local_addr,net_addr)
    session.add(abdomen)
    session.commit()
    session.close()