### Project Template README: Debug Odoo with Docker in VSCode

#### Overview
This project template facilitates Odoo development using Docker, specifically configured for VSCode IDE. It includes setup instructions and tips for effective debugging using the Odoo IDE extension.

#### VSCode with the following extensions:
   - Odoo IDE
   - Owl Vision
   - Odoo Shortcuts

#### Setup Steps

## Development

**Clone the Project**
```bash
git clone https://github.com/teguhteja/docker-odoo-dev.git -b 15
readme.excalidraw
readme.plantuml
.gitignore
.dockerignore
pyenv install 3.9.18
pyenv versions
pyenv local 3.9.18 # .python-version
# direnv, echo 'eval "$(direnv hook bash)"' >> ~/.zshrc
echo 'layout pyenv 3.9.18' > .envrc
direnv allow
source .direnv/python-3.9.18/bin/activate
# THIS doesnt need if .envrc/direnv is used
# python -m venv .venv 
# source .venv/bin/activate
pip install -r requirements.txt 
touch .env
GH action https://github.com/python-semantic-release/python-semantic-release
GH readme.md https://github.com/othneildrew/Best-README-Template

```

**Odoo Framework Integration for Visual Studio Code**
```bash
https://github.com/odoo-ide/vscode-odoo

```

**Python static analysis tool : Odoo Stubs**
```bash
git clone https://github.com/odoo-ide/odoo-stubs.git -b 15.0 odoo-stubs-15
```
pyrightconfig.json
```bash
{
    "stubPath": "./odoo-stubs15/",
    "extraPaths": [
        "./custom-addons/",
    ]
}
```

**Build Docker Image w/ pydevd-odoo debugger**
   ```bash
   https://github.com/odoo-ide/pydevd-odoo
   requirements.txt pydevd-odoo
   in Dockerfile
   - change image sourceand version based on which paltform you are developing
      arm macos -->FROM wbms/odoo-15.0
      arm macos -->FROM arm64v8/odoo:15.0
      x86 --> FROM odoo:15
   docker build --platform linux/arm64/v8,linux/amd64 -t odoodev:15 .
   ```

**Start Docker Compose**
   ```bash
   in docker-compose.yml
   - change version related parameters 
   --> platform: linux/amd64
   docker compose up -d
   ```

**Add Your Addons**
   `mkdir custom-addons`
   `docker compose restart odoo-dev`

**Debugging**
   - Set breakpoints in your source code within VSCode.
   - Ensure the debugger is configured to debug external code (`"justMyCode": false` in .vscode/launch.json).
   - Access the Odoo source code from the container:
     ```bash
     ./docker-cp-odoo.sh
     ```
   - Add breakpoints in the Odoo source code.
   - Run the debugger process to start debugging.

#### Troubleshooting Tips

**Copying misc.py in odoodev**
   If backup failures occur with Docker images, modify `misc.py` to resolve issues.

**Debugging Odoo Source Code**
   Modify `"justMyCode": false` in `launch.json`, 
   download the Odoo folder from the container using `docker-cp-odoo.sh`,
   uncomment this line in docker-compose.yml
   `- ./odoo:/usr/lib/python3/dist-packages/odoo` 
   restart stack or docker compose
   add breakpoints, and start the debugger process .

#### Conclusion
This README provides detailed steps to set up an Odoo development environment using Docker and VSCode, enabling efficient debugging of Odoo applications. For further details, refer to the full documentation and scripts available in the project repository.

---

For detailed scripts and further instructions, visit [docker-odoo-dev](https://github.com/teguhteja/docker-odoo-dev.git).




▶

10:19
How To Configure Odoo15 With Pycharm || Odoo 15 Development Tutorials
Odoo Mates

2

4:03
How To Configure Custom Addons Path In Odoo15
Odoo Mates

3

21:16
1. How To Create Module In Odoo 15 || Odoo 15 Development || Odoo 15 Technical Training
Odoo Mates

4

4:43
2. How To Add Icon Image For Module In Odoo 15 || Odoo 15 Development Tutorials
Odoo Mates

5

17:25
3. How To Define Models In Odoo 15 || Creating Database Tables In Odoo
Odoo Mates

6

17:28
4. How To Create Menu In Odoo 15 || Defining Menus in Odoo 15 Development
Odoo Mates

7

10:26
5. How To Create Window Action In Odoo || Actions In Odoo
Odoo Mates

8

11:57
6. How To Link Menu And Actions In Odoo || Odoo 15 Development Tutorials
Odoo Mates

9

11:48
7. How To Set Access Rights For Model In Odoo || Security In Odoo
Odoo Mates

10

6:54
8. How To Set Icon For Menu In Odoo || Odoo 15 Development Tutorials
Odoo Mates

11

20:17
9. How To Create Form View In Odoo 15 || Odoo 15 Development Tutorials
Odoo Mates

12

7:00
10. How To Define Tree View In Odoo 15 || List View in Odoo 15
Odoo Mates

13

14:00
11. How To Define Search View In Odoo || Odoo 15 Control Panel View
Odoo Mates

14

12:55
12. How To Add Filters And Group By Options In Odoo Search View || Odoo 15 Development Tutorials
Odoo Mates

15

10:12
13. How To Add Archive and Unarchive Options In Odoo || Odoo 15 Development Tutorials
Odoo Mates

16

10:03
14. How To Apply Domain For Menu In Odoo || Odoo 15 Development Tutorials
Odoo Mates

17

7:43
15. How To Set Default Value Using Context In Odoo || Context In Odoo
Odoo Mates

18

7:51
16. How To Set Default Filter And Group By In Odoo Search View || Odoo 15 Development
Odoo Mates

19

9:25
17. How To Add Chatter To Form View In Odoo || Add Chatter In Odoo
Odoo Mates

20

6:00
18. How To Enable Tracking For Fields In Odoo || Track Field Changes In Odoo || Audit Log Odoo
Odoo Mates

21

8:36
19. How To Add Search Panel In Odoo 15 || Odoo 15 Development Tutorials
Odoo Mates

22

15:25
20. How To Add Many2one Field In Odoo || Relational Fields in Odoo || Odoo 15 Development Tutorials
Odoo Mates

23

10:02
21. How To Add Date And Datetime Fields In Odoo || Odoo 15 Tutorials
Odoo Mates

24

7:17
22. How To Set Default Values For Fields In Odoo || Default Field Values || Odoo 15 Development
Odoo Mates

25

8:44
23. How To Add Related Fields In Odoo || Relational Fields In Odoo || Odoo 15 Tutorials
Odoo Mates

26

23:48
24. How To Create Computed Field In Odoo 15 || Compute Field In Odoo 15 || Odoo 15 Development
Odoo Mates

27

6:30
25. How To Define Onchange Functions In Odoo || Odoo 15 Onchange Fields || Odoo 15 Development
Odoo Mates

28

8:03
26. Understanding Rec Name In Odoo || Odoo Rec Name || Rec Name For Models in Odoo
Odoo Mates

29

10:15
27. How To Add Notebook And Pages In Odoo Form View || Odoo 15 Tutorials
Odoo Mates

30

5:54
28. How To Define HTML Field In Odoo 15 || Html Field In Odoo || Odoo15 Development Tutorials
Odoo Mates

31

8:54
29. Remove Create, Edit, Delete and Duplicate Options From Views In Odoo || Odoo Development Videos
Odoo Mates

32

7:45
30. Working Of Priority Widget In Odoo || Priority Widget In Odoo || Odoo 15 Development Videos
Odoo Mates

33

13:03
31. How To Add Statusbar In Odoo Development || Odoo 15 Development Tutorials
Odoo Mates

34

12:49
32. How To Add Buttons In Odoo || Odoo Button Types || Odoo 15 Development Tutorials
Odoo Mates

35

4:55
33. Show Confirmation Message On Button Click In Odoo || Odoo 15 Development Tutorials
Odoo Mates

36

7:36
34. How To Add Help Messages For Fields And Buttons In Odoo || Odoo 15 Development Tutorials
Odoo Mates

37

4:18
35. How To Fix Compute Method Failed To Assign Value Error In Odoo || Odoo Debugging
Odoo Mates

38

5:25
36. Rainbow Effect In Odoo 15 || Odoo Effects || Odoo 15 Development Tutorials
Odoo Mates

39

11:31
37. Badge Widget And Decorations In Odoo || Odoo Decorations || Widget Badge In Odoo || Odoo Widgets
Odoo Mates

40

7:09
38. How To Give Color For Tree View Records In Odoo || Tree View Color In Odoo || Odoo 15 Decoration
Odoo Mates

41

6:07
39. Widget List Activity In Odoo || List Activity Widget In Odoo || Activity in Odoo Tree View
Odoo Mates

42

6:49
40. Dynamic Tree View In Odoo || Optional Field Visibility In List View || Odoo 15 development
Odoo Mates

43

9:00
41. Many2one Avatar And Many2One Avatar User Widget In Odoo || Odoo 15 Widgets || Odoo 15 Tutorials
Odoo Mates

44

7:05
42. How To Make HTML Field Collaborative || Collaborative Html Fields In Odoo || Odoo 15 Development
Odoo Mates

45

3:02
43. How To Enable Resizable Option For Html Field In Odoo || Odoo 15 Development Tutorials
Odoo Mates

46

4:25
44.Default Focus Attribute In Odoo || Odoo 15 Development || Learn Odoo Development
Odoo Mates

47

4:43
45. How To Show Sample Data In Odoo Views || Display Sample Data in Odoo Views || Odoo Tips
Odoo Mates

48

4:09
46. How To Enable Multi Editing In Odoo Tree View || Odoo 15 Development Tutorials
Odoo Mates

49

17:58
47. How To Control Statusbar Using Buttons In Odoo 15 || Odoo 15 Workflow || Odoo 15 Development
Odoo Mates

50

6:52
48. Data Hot Key In Odoo 15 || Enable Button Shortcuts in Odoo || Odoo 15 Development Tutorials
Odoo Mates

51

20:43
49. One2many Field In Odoo 15 || Odoo Relational Fields || Odoo 15 Development Tutorials
Odoo Mates

52

3:04
50. Editable Top And Bottom Attribute In Odoo 15 || Odoo 15 Development Tutorials
Odoo Mates

53

7:15
51. Hide One2many Column Based On Parent Record In Odoo || Odoo 15 Development Tips || Odoo Tricks
Odoo Mates

54

5:43
52. How To Show Field Or Button Only In Developer Mode In Odoo || Odoo 15 Development Tutorials
Odoo Mates

55

6:39
53. How To Add Image Field In Odoo || Odoo 15 Development Tutorials
Odoo Mates

56

4:13
54. Widget Boolean Toggle In Odoo || Odoo 15 Development Tutorials
Odoo Mates

57

4:41
55. Color Picker Widget In Odoo 15 || Color Field in Odoo || Odoo 15 Development Tutorials
Odoo Mates

58

5:42
56. Widget Color In Odoo || Color Field In Odoo | Odoo 15 Development Tips and Tricks | Odoo Widgets
Odoo Mates

59

11:10
57. How To Add Many2many Field In Odoo15 || Odoo Relational Fields || Odoo 15 Development Tutorials
Odoo Mates

60

6:23
58. How To Enable Color Options For Many2many Field In Odoo || Odoo 15 Technical Training
Odoo Mates

61

11:20
59. How To Create Activity View In Odoo 15 || Advanced Odoo Development || Odoo 15 Development
Odoo Mates

62

3:34
60. How To Enable Code View In Odoo 15 HTML Fields || HTML Field Code View || Odoo 15 Development
Odoo Mates

63

9:21
61. Transient Model In Odoo || Odoo 15 Development Tutorials || Odoo Advanced Tutorials
Odoo Mates

64

13:37
62. Create And Launch Wizard In Odoo 15 || Odoo 15 Wizard || Odoo 15 Development Tutorials
Odoo Mates

65

2:35
63. How To Add Text Field In Odoo || Odoo 15 Development Tutorials || Odoo Advanced Tutorials
Odoo Mates

66

6:40
64. How To Launch Wizard From Button In Odoo | Return Wizard From Button in Odoo | Odoo Development
Odoo Mates

67

8:39
65. How To Load Data From XML File In Odoo | Odoo Data Files | Odoo 15 Tutorials | Data Files Odoo
Odoo Mates

68

5:15
66. Load Data From CSV File In Odoo || Data File in Odoo || Odoo 15 Tutorials || Odoo CSV Files
Odoo Mates

69

6:31
67. Create Module Using Scaffold Command In Odoo || Odoo Scaffold Command || Odoo Bin
Odoo Mates

70

6:08
68. How To Inherit Model In Odoo || Odoo Inheritance || Odoo 15 Tutorials || Odoo 15 Development
Odoo Mates

71

21:05
69. How To Inherit And Add Field To A Model In Odoo || Odoo Inheritance || Odoo 15 Tutorials
Odoo Mates

72

8:33
70. How To Inherit A Function In Odoo || Odoo Inheritance || Odoo 15 Tutorials | Odoo 15 Development
Odoo Mates

73

8:57
71. How To Override Create Method In Odoo || Odoo 15 Tutorial || Odoo ORM Methods
Odoo Mates

74

16:33
72. How To Create Sequence And Generate Sequential Value For Record In Odoo || Odoo 15 Tutorials
Odoo Mates

75

9:13
73. How To Override Write Method In Odoo || Inherit Write Function In Odoo || Odoo ORM Methods
Odoo Mates

76

10:00
74. Default Get Function In Odoo || Odoo Default Get Method || Odoo 15 Tutorial || Odoo ORM Methods
Odoo Mates

77

9:51
75. Name Get Function In Odoo || Odoo Name Get Method || Odoo 15 Tutorials || Odoo ORM Method
Odoo Mates

78

12:45
How To Run Odoo From Terminal | Odoo Command Line Options | Odoo CLI | How To Run Odoo Using Command
Odoo Mates

79

6:59
How To Generate Odoo Configuration File From Terminal || Odoo Command Line Interface || Odoo CLI
Odoo Mates

80

5:41
How To Install Module From Terminal In Odoo || Odoo Command Line Interface || Odoo CLI
Odoo Mates

81

5:50
Error no 98 Address Already In Use Error Odoo | Reason & Solution | Fix Address already In Use Error
Odoo Mates

82

4:03
How To Upgrade A Module From Odoo CLI || Upgrade Module From Terminal In Odoo || Odoo Command Line
Odoo Mates

83

5:36
How To Create Database From Terminal Odoo CLI || Odoo Command Line Interface || Odoo CLI Parameters
Odoo Mates

84

6:26
76. Menu And SubMenu Without Specifying Parent In Odoo || Odoo Tips and Tricks || Odoo Advanced
Odoo Mates

85

6:06
77. Target Inline In Odoo || Inline Actions In Odoo || Target In Odoo Actions || Odoo Window Action
Odoo Mates

86

31:26
Odoo Environment | Odoo Self | self.env in Odoo || Odoo Environment Variables
Odoo Mates

87

11:06
78. Active Id In Odoo Development || Odoo active_id || Get Data From Main Model inside Wizard Model
Odoo Mates

88

8:27
79. Hide Field Based On Context In Odoo | Odoo Context | Odoo 15 Tips and Tricks | Odoo 15 Tutorials
Odoo Mates

89

6:25
80. How To Raise Validation Error In Odoo || Odoo Validation || Validation Error In Odoo
Odoo Mates

90

13:35
81. Apply Domain For Fields In Odoo || Odoo Domain Concept || Odoo Field Domain || Odoo 15 Tutorials
Odoo Mates

91

15:06
82. Sql Constraints In Odoo || Constrains In Odoo || Odoo 15 Field Validations
Odoo Mates

92

7:15
83. Python Constrains In Odoo || Constrains Decorator In Odoo || Model Constrains In Odoo
Odoo Mates

93

12:32
84. Copy Function In Odoo | Copy Attribute In Odoo | Odoo Copy ORM Method
Odoo Mates

94

8:33
85. How To Override Unlink Method In Odoo || Prevent Deleting Record || Odoo Unlink ORM Method
Odoo Mates

95

12:53
86. Stored Compute Field In Odoo And Its Dependency || Re computation Of Stored Compute Field
Odoo Mates

96

2:58
87. How To Disable Export Excel Option From Odoo Tree View || Odoo 15 Development Tutorials
Odoo Mates

97

7:57
88. Ondelete Policy In Odoo | Ondelete Restrict and Ondelete Cascade In Odoo | Odoo Ondelete Policy
Odoo Mates

98

10:33
89. How To Hide Fields Based On Conditions In Odoo || Make Field Invisible Based On Other Fields
Odoo Mates

99

5:48
90. How To Make Field Readonly Based On Condition In Odoo || Conditional Readonly Fields In Odoo
Odoo Mates

100

8:01
91. How To Make Field Required Based On Conditions In Odoo || Conditional Required Fields In Odoo
Odoo Mates

101

4:17
92. Label Attribute In Odoo | Class oe_edit_only | Label For Fields | Edit Only Class In Odoo
Odoo Mates

102

5:55
93. How To Add Buttons In Tree View Header In Odoo || Button Near Create Button in Odoo
Odoo Mates

103

11:28
94. How To Add Buttons In Odoo Tree View || Set Icons For Buttons in Odoo || Odoo Button Classes
Odoo Mates

104

5:27
95. Ondelete Decorator In Odoo || Execute Codes On Deleting a Record In Odoo || Decorators in Odoo
Odoo Mates

105

8:14
96. How To Add Buttons Inside Group By Tree View In Odoo || Buttons in Group By List View
Odoo Mates

106

14:35
97. Handling And Debugging Odoo Errors | Manual Debugging | Odoo Errors | Trace Odoo Issues
Odoo Mates

107

20:51
98. How To Add Settings For Module In Odoo | Module Settings In Odoo | Configuration Menu In Odoo
Odoo Mates

108

12:26
99. How To Set Inverse Function For Computed Field In Odoo || Editable Compute Field In Odoo
Odoo Mates

109

14:22
100. Searchable Non Stored Compute Field In Odoo | How To Define Search Function For Field In Odoo
Odoo Mates

110

2:37
Radio Widget In Odoo || Show Selection Field as Radio Buttons || Odoo Widgets
Odoo Mates

111

5:04
Force Save Attribute In Odoo || Write Value To Readonly Field From Onchange Function
Odoo Mates

112

3:39
Widget Many2many Checkboxes and Many2many Tags In Odoo || Widgets in Odoo
Odoo Mates

113

2:39
Selection Widget In Odoo || Widget Selection In Odoo || Widgets In Odoo
Odoo Mates

114

12:00
How To Access Value From Settings In Odoo || Odoo Module Settings
Odoo Mates

115

3:56
Log Access Model Attribute In Odoo || Remove Create and Write Fields From Odoo Models
Odoo Mates

116

10:19
Name Create Function In Odoo || Odoo ORM Method || Use and Working of Name Create Function
Odoo Mates

117

9:17
How To Hide User Group From Users Form View In Odoo || Remove User Group From Users Form View
Odoo Mates

118

6:00
Aggregate Options In Odoo List View Odoo || Sum and Average in Odoo List View
Odoo Mates

119

4:16
Order Attribute In Odoo Models || How To Set Order For Records In Odoo || Odoo Model Attributes
Odoo Mates

120

4:25
How To Reload The Screen From Python Code In Odoo || Refresh Odoo Screen From Python Code in Odoo
Odoo Mates

121

8:21
Reference Field In Odoo || Odoo Reference Field || Odoo 15 Technical Training
Odoo Mates

122

14:37
How To Show Alerts In Odoo Form View || Alerts in Odoo || Alert Warning in Odoo | Alert Info In Odoo
Odoo Mates

123

7:23
Widget Phone || Widget Email || Widget URL In Odoo || Odoo Widgets
Odoo Mates

124

4:21
Widget Ace In Odoo || Mode Python and Mode XML || Odoo Technical Training Videos
Odoo Mates

125

12:14
Server Action In Odoo || Add Action To Action Button In Odoo || Odoo Server Action
Odoo Mates

126

17:01
Progress Widgets In Odoo | Gauge Widget - ProgressBar Widget - Percentpie Widget | Graphical Widgets
Odoo Mates

127

28:39
Calendar View In Odoo || Odoo Calendar View || Views In Odoo || Odoo Advanced Views
Odoo Mates

128

19:53
Read Group Method In Odoo || Odoo Read Group Method || Odoo ORM Methods
Odoo Mates

129

13:38
How To Add Stat Buttons In Odoo || Odoo Smart Buttons || Odoo Technical Training
Odoo Mates

130

8:56
Widget Handle In Odoo || Drag and Change Records In Tree View || Odoo Development Tutorials
Odoo Mates

131

21:25
Basics Of PostgreSQL Query || Odoo Queries || PSQL Insert, Update, Select and Delete Queries
Odoo Mates

132

22:45
Monetary Field And Widget Monetary In Odoo || Odoo Currency Fields
Odoo Mates

133

8:18
How To Change Order Of Tracking Values In Odoo || Enable Ordered Tracking For Fields In Odoo
Odoo Mates

134

11:50
URL Action In Odoo || Redirect To URL From Code || Odoo URL Actions
Odoo Mates

135

9:00
Bold Text in Odoo Tree || Italic Text In Odoo Tree View || Color In Odoo Tree View For Column
Odoo Mates

136

15:09
NoUpdate Attribute In Odoo || ForceCreate Attribute In Odoo || Odoo Noupdate and Forcecreate
Odoo Mates

137

17:11
Odoo Whatsapp Integration || Odoo Whatsapp Connector || Redirect To Whatsapp From Odoo
Odoo Mates

138

16:25
Customize PDF Reports From User Interface In Odoo
Odoo Mates

139

6:43
Odoo Create ORM Method | Odoo ORM Methods
Odoo Mates

140

7:48
Odoo Browse ORM Method | Odoo ORM Methods
Odoo Mates

141

4:22
Odoo Write ORM Method || Odoo ORM Methods
Odoo Mates

142

3:06
Odoo Unlink ORM Method || Odoo ORM Documentation
Odoo Mates

143

10:20
Odoo Search ORM Method || Odoo ORM Tutorial
Odoo Mates

144

5:22
Odoo Search Count ORM Method || Odoo ORM documentation
Odoo Mates

145

6:18
Odoo Get Metadata || Odoo ORM Methods
Odoo Mates

146

4:41
Odoo Fields Get || Odoo ORM Method
Odoo Mates

147

3:36
Trim Field Attribute In Odoo || Odoo 15 Development
Odoo Mates

148

11:57
Odoo Shell Command | Odoo Python Console | Odoo Shell
Odoo Mates

149

10:06
How To Pass New Field Value From Sale Order To Invoice In Odoo
Odoo Mates

150

10:53
How To Inherit And Add Field To One2many Field In Odoo
Odoo Mates

151

5:02
How To Fix Invoice Line Value Missing On Saving issue || Adding Field in Invoice Line
Odoo Mates

152

1:40
Kebab Menu In Odoo
Odoo Mates

153

5:46
Active Test In Odoo || Odoo Active Test
Odoo Mates

154

6:35
Prevent Closing Of Wizard In Odoo
Odoo Mates

155

10:20
Decimal Accuracy In Odoo || Decimal Precision In Odoo
Odoo Mates

156

3:05
How To Fix Not A Valid Action On The Model Error In Odoo
Odoo Mates

157

14:12
Display Notification In Odoo || Notifications In Odoo
Odoo Mates

158

4:25
How To Get Code From Postman Application || Postman Code Generator
Odoo Mates

159

18:14
Basic Ubuntu Commands || Useful Ubuntu Commands
Odoo Mates

160

1:21
Sponsor Odoo Mates In Github || Github Sponsorship
Odoo Mates

161

4:48
Odoo Message Post Function || Add Message To Chatter From Code in Odoo
Odoo Mates

162

14:46
Install Odoo 15 In Cloud Server || Odoo Installation Scrypt || Odoo Installation Steps
Odoo Mates

163

5:31
Fix Connection Lost and Connection Restored Error Odoo || Odoo Workers
Odoo Mates

164

7:00
How To Enable Multi Processing In Odoo | Configure Workers In Odoo
Odoo Mates

165

8:53
How To Copy Files To Remote Server Using SCP Command || Ubuntu SCP || File Transfer
Odoo Mates

166

9:59
How To Setup Custom Addons Path In Odoo Server || Configure Custom Addons Path
Odoo Mates

167

6:09
Return Action With Sticky Notification In Odoo || Odoo Sticky Notification
Odoo Mates

168

7:29
How To Install Third Party Modules In Odoo Instance || Install Module From Odoo App Store
Odoo Mates

169

4:21
How To Configure Domain Name For Odoo Instance || Odoo Deployment
Odoo Mates

170

8:06
How To Configure SSL For Domain | Enable Https For Odoo Instance | Secure Nginx with Let's Encrypt
Odoo Mates

171

11:24
How To Execute SQL Queries In Odoo || Query Execution In Odoo
Odoo Mates

172

11:55
Inherit And Add Chatter To Existing Models In Odoo || Odoo Chatter
Odoo Mates

173

4:41
Excludes Attribute In Odoo || Prevent Module Installation If Module Installed
Odoo Mates

174

11:54
How To Add New Field To Sale Report Model In Odoo || Inherit Database View In Odoo
Odoo Mates

175

11:19
Odoo External API | Authentication From External Application | Odoo External API Logging in
Odoo Mates

176

14:02
Odoo External API: Search And Read From Odoo Database
Odoo Mates

177

5:06
Odoo XMLRPC: Search Read Method To Read From Database
Odoo Mates

178

5:47
Create Record In Odoo From External Applications | Odoo External API
Odoo Mates

179

6:45
Write Into Odoo Database From External Application || Odoo External API
Odoo Mates

180

5:18
How To Delete Records From Odoo Database Using External API
Odoo Mates

181

1:41
Odoo Mates PlayGround || Odoo Mates Query Execution
Odoo Mates

182

21:20
Create PDF And Excel Reports In Odoo 15 || Odoo 15 Excel Reporting | Odoo 15 PDF Reports
Odoo Mates

183

13:41
How To Generate Line No For One2many Fields In Odoo
Odoo Mates

184

9:03
How To Add Line Number In Odoo Qweb Report | Line Number Inside For Loop
Odoo Mates

185

10:50
How To Add Barcode And QR Code In Odoo PDF Reports
Odoo Mates

186

6:58
Read Data From Odoo Database And Write Into A CSV File Using Python Scrypt
Odoo Mates

187

26:49
How To Create Email Template In Odoo || Odoo Email Templates
Odoo Mates

188

13:01
How To Send Email From Odoo Using Email Template || Sending Emails From Odoo Using Code
Odoo Mates

189

8:06
How To Inherit a Super Function In Odoo || How To Override a Inherited Function In Odoo
Odoo Mates



Show chat replay

