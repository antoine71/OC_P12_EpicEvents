API_ENDPOINTS = [
    {
        'path': '/api/clients/',
        'methods':
            [
                {
                    'name': 'get',
                    'permissions': ('all', ),
                },
                {
                    'name': 'post',
                    'permissions': ('sales', ),
                },
            ],
    },
    {
        'path': '/api/clients/1/',
        'methods':
            [
                {
                    'name': 'get',
                    'permissions': ('all', ),
                },
                {
                    'name': 'put',
                    'permissions': ('sales_user', ),
                },
                {
                    'name': 'delete',
                    'permissions': ('sales_user', ),
                },
            ],
    },
    {
        'path': '/api/clients/1/add_contract/',
        'methods':
            [
                {
                    'name': 'post',
                    'permissions': ('sales_user', ),
                },
            ],
    },
    {
        'path': '/api/contracts/',
        'methods':
            [
                {
                    'name': 'get',
                    'permissions': ('all', ),
                },
            ],
    },
    {
        'path': '/api/contracts/1/',
        'methods':
            [
                {
                    'name': 'get',
                    'permissions': ('all', ),
                },
                {
                    'name': 'put',
                    'permissions': ('sales_user', ),
                },
                {
                    'name': 'delete',
                    'permissions': ('sales_user', ),
                },
            ],
    },
    {
        'path': '/api/contracts/2/add_event/',
        'methods':
            [
                {
                    'name': 'post',
                    'permissions': ('sales_user', ),
                },
            ],
    },
    {
        'path': '/api/events/',
        'methods':
            [
                {
                    'name': 'get',
                    'permissions': ('all', ),
                },
            ],
    },
    {
        'path': '/api/events/1/',
        'methods':
            [
                {
                    'name': 'get',
                    'permissions': ('all', ),
                },
                {
                    'name': 'put',
                    'permissions': ('support_user', ),
                },
                {
                    'name': 'delete',
                    'permissions': ('support_user', ),
                },
            ],
    },
]
