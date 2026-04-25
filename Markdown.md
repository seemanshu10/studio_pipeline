# OpenSource Studio Pipeline

## 📌 Objective
A lightweight, scalable studio pipeline designed to handle daily production workflows in VFX and game studios.  
It manages:

- Asset creation  
- Shot creation  
- Folder structures  
- Publishing workflows  
- Dependency organization  

The goal is to provide a **simple, flexible system** that works for both small teams and large productions.

---

## 🎯 Target Users
- VFX Studios  
- Game Development Studios  
- Freelancers & Small Teams  
- Pipeline TDs looking for customizable infrastructure  

---

## 🚀 Core Features

### 1. Easy Setup
- One-time initialization of the pipeline
- Works across different environments
- CLI-based execution (supports `.bat` scripts)

### 2. Scalable Architecture
- Supports multiple projects
- Modular structure for easy expansion
- Suitable for both small and large teams

---

## ⚙️ Functional Features

### 📁 1. Folder Creation via JSON Templates
- Folder structures are defined in JSON template files
- Dynamic generation based on user input
- Ensures consistency across projects

![folderStructure.png width="20" height="10](image_files\folderCreation.PNG)

---

### 📦 2. Publish System (Version Controlled)
- Files are published into a **Published** directory
- Published files:
  - **Cannot be overwritten**
  - Always create a **new version**
- Automatic versioning:
  - Detects latest version
  - Increments version (e.g., `v001 → v002`)

---

### 🧠 3. Edge Case Handling
- Missing folders → auto-create  
- Naming conflicts → resolved via rules  
- Invalid inputs → validated before execution  
- Safe publishing → prevents accidental overwrites  

---

## 🛠️ Technology Stack

- **Language:** Python  
- **Data Format:** JSON  
- **Execution:** CLI / Batch Scripts  

---

## 🧩 Core System Architecture

### 🏗️ Studio Root Structure

```
STUDIO_PIPELINE/
│
├── PROJECTS/        # Active and archived projects
├── LIBRARY/         # Reusable assets (HDRIs, rigs, textures)
├── PIPELINE_TOOLS/  # Python tools and scripts
├── TEMPLATES/       # JSON folder templates
└── CONFIG/          # Naming rules, constants, settings
```

---

## 🔁 Core Logic Flow

### 1. Pipeline Initialization
- Setup studio structure using base templates
- Configure global settings


### 2. Project Creation
- User selects a template
- System generates project structure inside `PROJECTS/`



### 3. Asset & Shot Creation
- Assets and shots are created using template definitions
- Automatically structured and named



### 4. Publish Workflow
- User selects a file to publish
- System:
  1. Detects latest version
  2. Increments version
  3. Saves to publish directory
  4. Locks previous versions



## 🧠 Backend Logic

### CLI-Based System
- Fully operable via command line
- Can be integrated into `.bat` scripts
- Example operations:
  - Initialize pipeline
  - Create project
  - Create asset
  - Publish file

---

### Data-Driven Design
- JSON templates define:
  - Folder structures
  - Naming conventions
  - Asset types

---

## 🖥️ UI Frontend (Optional Layer)

### Features
- Input fields:
  - Project Name
  - Asset Name
  - Shot Name

- Actions:
  - Create Project
  - Create Asset
  - Publish File

### Publish Button
- Takes selected file
- Sends it to backend
- Triggers versioned publish system

---

## 🔄 Versioning Strategy

Example:

```
character_model_v001.ma
character_model_v002.ma
character_model_v003.ma
```

Rules:
- Always increment version
- Never overwrite existing files
- Automatically detect latest version

---

## 📦 Templates System

### Location
```
folder_template/
```

### Purpose
- Define folder structures
- Standardize pipeline across projects

### Example (Concept)
```json
{
  "Project": {
    "Assets": {},
    "Sequences": {},
    "Publish": {},
    "Cache": {},
    "Renders": {}
  }
}
```

---

## ⚡ Key Advantages

- 🔹 Simple and fast setup  
- 🔹 Fully customizable via JSON  
- 🔹 Safe publishing workflow  
- 🔹 Scalable for production environments  
- 🔹 CLI + optional UI support  

---

## 🔮 Future Improvements (Optional)

- GUI Dashboard  
- Database integration (optional later)  
- Asset dependency tracking  
- Render farm integration  
- User permission system  
