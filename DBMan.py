from Database import DBSession,Brain,Abdomen,Iris,Lung_CR,Lung_CT, Picture


def insertBrain(local_addr,net_addr):
    session = DBSession()
    try:
        lung = Brain(local_addr=local_addr, net_addr=net_addr)
        session.add(lung)
        session.commit()
    except Exception, e:
        print 'insert lung_CR error:', e
    session.close()

def insertLung_CT(local_addr,net_addr):
    session = DBSession()
    try:
        lung = Lung_CT(local_addr=local_addr, net_addr=net_addr)
        session.add(lung)
        session.commit()
    except Exception, e:
        print 'insert lung_CR error:', e
    session.close()

def insertLung_CR(local_addr,net_addr):
    session = DBSession()
    try:
        lung = Lung_CR(local_addr=local_addr, net_addr=net_addr)
        session.add(lung)
        session.commit()
    except Exception, e:
        print 'insert lung_CR error:', e
    session.close()

def insertIris(local_addr,net_addr):
    session = DBSession()
    try:
        pupil = Iris(local_addr=local_addr, net_addr=net_addr)
        session.add(pupil)
        session.commit()
    except Exception, e:
        print 'insert iris error:', e
    session.close()

def insertAbdomen(local_addr, net_addr):
    session = DBSession()
    try:
        abdomen = Abdomen(local_addr=local_addr, net_addr=net_addr)
        session.add(abdomen)
        session.commit()
    except Exception, e:
        print "insert abdomen error:", e
    session.close()

def insertPicture(local_addr, net_addr, artical_url):
    session = DBSession()
    try:
        picture = Picture(local_addr, net_addr, artical_url)
        session.add(picture)
        session.commit()
    except Exception, e:
        print 'insert picture error:',e
    session.close()