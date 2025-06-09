import pytest

def test_infer_db_type_hive():
    from library.hive_table import infer_db_type
    assert infer_db_type("HiveProdDSN") == "hive"

def test_infer_db_type_impala():
    from library.hive_table import infer_db_type
    assert infer_db_type("ImpalaProd") == "impala"

def test_infer_db_type_postgres():
    from library.hive_table import infer_db_type
    assert infer_db_type("PostgresDSN") == "postgresql"
