# Studio_pipeline

What Studio_template has :
PROJECTS → all active projects
LIBRARY → reusable assets (HDRI, rigs, textures)
PIPELINE_TOOLS → your Python scripts
TEMPLATES → folder templates
CONFIG → naming rules, settings

## Inside PROJECTS:

PROJECTS/
└── Project_Name/
    ├── assets/
    ├── sequences/
    ├── shots/
    ├── renders/
    ├── publish/
    └── work/

## ASSET STRUCTURE (VERY IMPORTANT)
assets/
└── character/
    └── hero_character/
        ├── model/
        ├── rig/
        ├── texture/
        ├── lookdev/
        ├── publish/
        └── work/

### repeat for 

- prop
- environment 
- vehicle

## SHOT STRUCTURE (VFX STYLE)

'''
sequences/
└── seq001/
    └── shot010/
        ├── animation/
        ├── layout/
        ├── lighting/
        ├── fx/
        ├── comp/
        ├── cache/
        ├── publish/
        └── work/

'''

## Inside assets:

environment/
└── building_A/
    ├── high/
    ├── mid/
    ├── low/
    ├── textures/
    ├── engine/
    └── publish/


#### Rules
- work = editable
- Publish = locked 