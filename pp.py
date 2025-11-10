#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            banner=dict(type='str', required=True)
        )
    )

    banner = module.params['banner']
    module.exit_json(changed=False, msg=f"Banner is: {banner}")

if __name__ == "__main__":
    main()



