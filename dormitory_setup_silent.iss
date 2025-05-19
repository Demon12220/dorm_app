#define MyAppName "Система управления общежитием"
#define MyAppVersion "1.0"
#define MyAppPublisher "Olga"
#define MyAppURL ""
#define MyAppExeName "app_desktop.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
AppId={{F70E8056-3E6E-4E23-9F3D-39D88AF3C17F}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=output
OutputBaseFilename=dormitory_setup_silent
SetupIconFile=dormitory.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
; Следующие параметры добавлены для тихой установки
DisableWelcomePage=yes
DisableReadyPage=yes
DisableFinishedPage=yes

[Languages]
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "dist\app_desktop\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\app_desktop\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

; Создание дополнительной [Code] секции для поддержки тихой установки
[Code]
// Функция для определения параметров командной строки
function GetCommandlineParam (inParam: String): String;
var
  i: Integer;
  paramName: String;
  paramValue: String;
begin
  paramName := '';
  paramValue := '';
  
  for i := 1 to ParamCount do begin
    if Pos('/', ParamStr(i)) = 1 then begin
      if paramName <> '' then begin
        if CompareText(paramName, inParam) = 0 then begin
          Result := paramValue;
          Exit;
        end;
      end;
      paramName := Copy(ParamStr(i), 2, Length(ParamStr(i)) - 1);
      paramValue := '';
    end else begin
      if paramValue = '' then
        paramValue := ParamStr(i)
      else
        paramValue := paramValue + ' ' + ParamStr(i);
    end;
  end;
  
  if (paramName <> '') and (CompareText(paramName, inParam) = 0) then begin
    Result := paramValue;
    Exit;
  end;
  
  Result := '';
end;

// Функция запускается при инициализации установщика
function InitializeSetup: Boolean;
var
  silent: String;
begin
  silent := GetCommandlineParam('silent');
  if CompareText(silent, 'yes') = 0 then begin
    SetupMessage(msgWizardPreparing,'');
    SetupMessage(msgStatusExtractFiles,'');
    SetupMessage(msgStatusCreateIcons,'');
  end;
  Result := True;
end;
