### .vscode/launch.json [coder:save]
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug Sidebar Component",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:5173",
      "webRoot": "${workspaceFolder}/frontend/src",
      "sourceMaps": true,
      "trace": true,
      "sourceMapPathOverrides": {
        "webpack:///src/*": "${webRoot}/*"
      }
    }
  ]
}
```
[coder:end]