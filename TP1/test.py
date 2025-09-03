import pytest
import fonctions as f

def test_1_puissance_positif_et_nombre_positif():
    assert f.puissance_nombre(2, 3) == 8       
    assert f.puissance_nombre(4, 2) == 16       
    assert f.puissance_nombre(10, 1) == 10      

def test_2_puissance_positif_et_nombre_negatif():
    assert f.puissance_nombre(-3, 2) == 9       
    assert f.puissance_nombre(-2, 3) == -8      
    assert f.puissance_nombre(-1, 4) == 1       
    assert f.puissance_nombre(-1, 5) == -1      

def test_3_puissance_positif_et_nombre_nul():
    for x in [1, 3, 10, 100, 1000, 10000]:
        assert f.puissance_nombre(0, x) == 0     

def test_4_puissance_positif_et_nombre_virgule():
    assert f.puissance_nombre(9, 0.5) == 3.0
    assert f.puissance_nombre(16, 0.25) == 2.0
    assert f.puissance_nombre(27, 1.0) == 27.0



def test_5_puissance_nulle_et_nombre_positif():
    assert f.puissance_nombre(1, 0) == 1
    assert f.puissance_nombre(100, 0) == 1
    assert f.puissance_nombre(1.5, 0) == 1
    assert f.puissance_nombre(99.99, 0) == 1

def test_6_puissance_nulle_et_nombre_negatif():
    assert f.puissance_nombre(-1, 0) == 1
    assert f.puissance_nombre(-999, 0) == 1
    assert f.puissance_nombre(-2.5, 0) == 1
    assert f.puissance_nombre(-1234.56, 0) == 1

def test_7_puissance_nulle_et_nombre_nul():
    with pytest.raises(ValueError):
        assert f.puissance_nombre(0, 0)



def test_8_puissance_negatif_et_nombre_positif():
    assert f.puissance_nombre(4, -1) == 0.25    
    assert f.puissance_nombre(10, -2) == 0.01  
    assert f.puissance_nombre(2, -3) == 0.125   

def test_9_puissance_negatif_et_nombre_negatif():
    assert f.puissance_nombre(-2, -2) == 0.25   
    assert f.puissance_nombre(-2, -3) == -0.125 
    assert f.puissance_nombre(-1, -1) == -1     

def test_10_puissance_negatif_et_nombre_nul():
    with pytest.raises(ValueError):
        assert f.puissance_nombre(0, -2)               
    with pytest.raises(ValueError):
        assert f.puissance_nombre(0, -10)              

def test_11_puissance_negatif_et_nombre_virgule():
    assert f.puissance_nombre(4.0, -1) == 0.25
    assert f.puissance_nombre(9.0, -0.5) == 1/3
    assert f.puissance_nombre(16.0, -0.25) == 0.5



def test_12_puissance_virgule_et_nombre_positif():
    assert f.puissance_nombre(2.5, 2) == 6.25
    assert f.puissance_nombre(3.5, 3) == 42.875
    assert f.puissance_nombre(1.2, 4) == 2.0736

def test_13_puissance_virgule_et_nombre_negatif():
    assert f.puissance_nombre(-2.5, 2) == 6.25
    assert f.puissance_nombre(-2.0, 3) == -8.0

def test_14_puissance_virgule_et_nombre_nul():
    assert f.puissance_nombre(2.5, 0) == 1
    assert f.puissance_nombre(-3.5, 0) == 1
    assert f.puissance_nombre(0.0, 3) == 0

def test_15_puissance_virgule_et_nombre_virgule():
    assert f.puissance_nombre(2.0, 0.5) == 2 ** 0.5
    assert f.puissance_nombre(5.0, 2.0) == 25.0
    assert f.puissance_nombre(10.1, 1.0) == 10.1



def test_16_puissance_virgule_et_nombre_zero_negatif():
    with pytest.raises(ValueError):
        assert f.puissance_nombre(0.0, -1.5)
    with pytest.raises(ValueError):
        assert f.puissance_nombre(0.0, -0.1)
