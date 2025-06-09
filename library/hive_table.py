#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import logging
import pyodbc

def infer_db_type(dsn):
    """Infer database type based on DSN name"""
    dsn_lower = dsn.lower()
    if 'impala' in dsn_lower:
        return 'impala'
    elif 'postgres' in dsn_lower or 'pgsql' in dsn_lower:
        return 'postgresql'
    return 'hive'

def run_module():
    module_args = dict(
        dsn=dict(type='str', required=False),
        rest_api=dict(type='dict', required=False),
        create_stmt=dict(type='str', required=False),
        database=dict(type='dict', required=False),
        clone_on_change=dict(type='bool', default=False),
        allow_partial_copy=dict(type='bool', default=False),
        dry_run=dict(type='bool', default=False),
        log_file=dict(type='str', default='/var/log/hive_table_ansible.log'),
        email_alert=dict(type='dict', required=False)
    )

    result = dict(changed=False, message='')

    module = AnsibleModule(argument_spec=module_args, required_one_of=[['dsn', 'rest_api']], supports_check_mode=True)

    log_path = module.params['log_file']
    logging.basicConfig(filename=log_path, level=logging.INFO)

    if module.params['dsn']:
        dsn = module.params['dsn']
        db_type = infer_db_type(dsn)
        result['message'] = f"Detected DB type: {db_type.upper()} from DSN: {dsn}"
    else:
        result['message'] = "Using REST API — DB type assumed Hive Metastore"

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
