import os, io, sys, zipfile, base64, random, shutil, subprocess, tempfile, string, lzma, marshal, autopep8, time, bz2, zlib, gzip
from pathlib import Path
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# =================================================================
#                         BOT CONFIGURATION
# =================================================================
# Get bot token from user input at runtime
def get_bot_token():
    print("\n" + "="*50)
    print("🤖 TELEGRAM BOT SETUP")
    print("="*50)
    token = input("Please enter your Telegram Bot Token: ").strip()
    
    # Validate token format (basic check)
    if not token or ":" not in token:
        print("❌ Invalid token format. Please enter a valid bot token.")
        return get_bot_token()
    
    return token

# Initialize bot token
BOT_TOKEN = get_bot_token()
ALLOWED_USERS = []  # Empty list means all users are allowed.
# =================================================================

# =================================================================
#                         UTILITY FUNCTIONS
# =================================================================

def generate_random_suffix(length=10):
    """Generates a random numerical suffix."""
    characters = string.ascii_uppercase + string.digits
    return ''.join(str(random.randint(1, 10)) for _ in range(length))

def gw(length):
    """Generates a random lowercase word."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def remove_comments(input_file, output_file):
    """Removes C-style block comments (/* */) from a file."""
    with open(input_file, 'r') as input_f:
        content = input_f.read()
    output_content = ''
    in_comment = False
    i = 0
    while i < len(content):
        if content[i:i+2] == '/*':
            in_comment = True
            i += 2
            continue
        elif content[i:i+2] == '*/':
            in_comment = False 
            i += 2
            continue
        if not in_comment:
            output_content += content[i]
        i += 1
    with open(output_file, 'w') as output_f:
        output_f.write(output_content)

status_messages = [
    "\x1b[1;93m🔥 IGNITING ENCRYPTION ENGINES... 🚀",
    "\x1b[1;94m🛠️ WEAVING OBFUSCATION MAGIC... ✨",
    "\x1b[1;95m⚙️ SPINNING UP CODE SHIELD... 🛡️",
    "\x1b[1;96m🌌 DIVING INTO THE ENCRYPTION GALAXY... 🌠",
    "\x1b[1;92m🔒 LOCKING CODE IN A DIGITAL VAULT... 🔐",
    "\x1b[1;91m💻 CRUNCHING BYTES AT LIGHTSPEED... ⚡",
    "\x1b[1;93m🧙‍♂️ CASTING PYTHONIC ENCRYPTION SPELLS... 🪄",
    "\x1b[1;94m📦 PACKAGING CODE IN STEALTH MODE... 🕵️",
    "\x1b[1;95m🔍 SCRAMBLING CODE BEYOND RECOGNITION... 🌀",
    "\x1b[1;96m🚀 LAUNCHING HYPERDRIVE... 🌟"
]

def display_status():
    """Prints a random, colorful status message."""
    print(random.choice(status_messages))
    time.sleep(random.uniform(0.3, 0.8))

# =================================================================
#                    CYTHON COMPILATION ENGINE (G)
# =================================================================

def g(name, file_path):
    """
    Performs the Cython compilation steps and creates the intermediate Python wrapper.
    """
    w = open(f"m/{name}", "r", encoding="utf-8")
    a = w.read()
    w.close()
    
    a = """#THIS ENCODE BY Aotpy | @Aotpy •
    exec(bytes([35,32,83,111,117,114,99,101,32,71,101,110,101,114,97,116,101,100,32,119,105,116,104,32,68,101,99,111,109,112,121,108,101,43,43,10,35,32,70,105,108,101,58,32,100,101,99,95,68,69,86,73,76,46,112,121,32,40,80,121,116,104,111,110,32,51,46,57,41,10,10,10,35,69,114,114,111,114,32,100,101,99,111,109,112,121,108,105,110,103,32,100,101,99,95,68,69,86,73,76,46,112,121,58,32,116,101,109,112,111,114,97,114,121,32,110,111,116,32,99,111,109,112,105,108,101,100]).decode())
    import os
    os.system('clear')\n""" + a
    
    print("\x1b[1;92m\x1b[38;5;49mENC PROCESS: INITIALIZING ENCRYPTION...!!")
    display_status()
    
    aa = autopep8.fix_code(a)
    os.remove(f"m/{name}")
    with open(f"m/{name}", 'w') as output_f:
        output_f.write(aa)
        
    print("\x1b[1;92m\x1b[38;5;48mENC PROCESS: INJECTING CYTHON LAYER...!!")
    display_status()
    
    os.system(f"cython m/{name}")
    
    name2 = name.replace(".py", ".c")
    
    try:
        with open(f"m/{name2}", "r") as f:
            if len(f.read()) < 1000:
                print("\x1b[1;91m❌ CYTHON COMPILATION FAILED! ABORTING... 😢")
                raise Exception("Cython compilation failed, output file too small.")
    except FileNotFoundError:
        raise Exception("Cython did not generate the C file.")
        
    remove_comments(f"m/{name2}", f"m/{name2}")
    display_status()
    
    name2_no_ext = name.replace(".py", "")
    
    # Custom C code entry point
    c = f'''
#ifdef __FreeBSD__
#include <dede.h>
#endif
#if PY_MAJOR_VERSION < 3
int main(int argc, char** argv) {{
#elif defined(Win32) || defined(MS_WINDOWS)
int wmain(int argc, wchar_t **argv) {{
#else
static int __Pyx_main(int argc, wchar_t **argv) {{
#endif
#ifdef __FreeBSD__
    fp_except_t m;
    m = fpgetmask();
    fpsetmask(m & ~FP_X_OFL);
#endif
    if (argc && argv)
        Py_SetProgramName(argv[0]);
    Py_Initialize();
    if (argc && argv)
        PySys_SetArgv(argc, argv);
    {{
      PyObject* m = NULL;
      __pyx_module_is_main_{name2_no_ext} = 1;
      #if PY_MAJOR_VERSION < 3
          init{name2_no_ext}();
      #elif CYTHON_PEP489_MULTI_PHASE_INIT
          m = PyInit_{name2_no_ext}();
          if (!PyModule_Check(m)) {{
              PyModuleDef *mdef = (PyModuleDef *) m;
              PyObject *modname = PyUnicode_FromString("__main__");
              m = NULL;
              if (modname) {{
                  m = PyModule_NewObject(modname);
                  Py_DECREF(modname);
                  if (m) PyModule_ExecDef(m, mdef);
              }}
          }}
      #else
          m = PyInit_{name2_no_ext}();
      #endif
      if (PyErr_Occurred()) {{
          PyErr_Print();
          #if PY_MAJOR_VERSION < 3
          if (Py_FlushLine()) PyErr_Clear();
          #endif
          return 1;
      }}
      Py_XDECREF(m);
    }}
#if PY_VERSION_HEX < 0x03060000
    Py_Finalize();
#else
    if (Py_FinalizeEx() < 0)
        return 2;
#endif
    return 0;
}}
#if PY_MAJOR_VERSION >= 3 && !defined(Win32) && !defined(MS_WINDOWS)
#include <locale.h>
static wchar_t*
__Pyx_char2wchar(char* arg)
{{
    wchar_t *res;
#ifdef HAVE_BROKEN_MBSTOWCS
    size_t argsize = strlen(arg);
#else
    size_t argsize = mbstowcs(NULL, arg, 0);
#endif
    size_t count;
    unsigned char *in;
    wchar_t *out;
#ifdef HAVE_MBRTOWC
    mbstate_t mbs;
#endif
    if (argsize != (size_t)-1) {{
        res = (wchar_t *)malloc((argsize+1)*sizeof(wchar_t));
        if (!res)
            goto oom;
        count = mbstowcs(res, arg, argsize+1);
        if (count != (size_t)-1) {{
            wchar_t *tmp;
            for (tmp = res; *tmp != 0 &&
                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)
                ;
            if (*tmp == 0)
                return res;
        }}
        free(res);
    }}
#ifdef HAVE_MBRTOWC
    argsize = strlen(arg) + 1;
    res = (wchar_t *)malloc(argsize*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    memset(&mbs, 0, sizeof mbs);
    while (argsize) {{
        size_t converted = mbrtowc(out, (char*)in, argsize, &mbs);
        if (converted == 0)
            break;
        if (converted == (size_t)-2) {{
            fprintf(stderr, "unexpected mbrtowc result -2");
            free(res);
            return NULL;
        }}
        if (converted == (size_t)-1) {{
            *out++ = 0xdc00 + *in++;
            argsize--;
            memset(&mbs, 0, sizeof mbs);
            continue;
        }}
        if (*out >= 0xd800 && *out <= 0xdfff) {{
            argsize -= converted;
            while (converted--)
                *out++ = 0xdc00 + *in++;
            continue;
        }}
        in += converted;
        argsize -= converted;
        out++;
    }}
#else
    res = (wchar_t *)malloc((strlen(arg)+1)*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    while(*in)
        if(*in < 128)
            *out++ = *in++;
        else
            *out++ = 0xdc00 + *in++;
    *out = 0;
#endif
    return res;
oom:
    fprintf(stderr, "out of memory");
    return NULL;
}}
int
main(int argc, char **argv)
{{
    if (!argc) {{
        return __Pyx_main(0, NULL);
    }}
    else {{
        int i, res;
        wchar_t **argv_copy = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        wchar_t **argv_copy2 = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        char *oldloc = strdup(setlocale(LC_ALL, NULL));
        if (!argv_copy || !argv_copy2 || !oldloc) {{
            fprintf(stderr, "out of memory");
            free(argv_copy);
            free(argv_copy2);
            free(oldloc);
            return 1;
        }}
        res = 0;
        setlocale(LC_ALL, "");
        for (i = 0; i < argc; i++) {{
            argv_copy2[i] = argv_copy[i] = __Pyx_char2wchar(argv[i]);
            if (!argv_copy[i]) res = 1;
        }}
        setlocale(LC_ALL, oldloc);
        free(oldloc);
        if (res == 0)
            res = __Pyx_main(argc, argv_copy);
        for (i = 0; i < argc; i++) {{
#if PY_VERSION_HEX < 0x03050000
            free(argv_copy2[i]);
#else
            PyMem_RawFree(argv_copy2[i]);
#endif
        }}
        free(argv_copy);
        free(argv_copy2);
        return res;
    }}
}}
#endif
'''
    # Read the Cython-generated C code and append the custom main/entry point
    with open(f"m/{name2}", 'r') as input_f:
        # The """ is appended to terminate the C code string in the wrapper
        co = input_f.read() + c + "\"\"\"" 
        
    cython_wrapper_name = file_path.replace('.py', '') + "-Aotpy-CYTHON-WRAPPER.py"
    
    # Python code for the inner Cython wrapper (responsible for compilation and execution)
    a_wrapper=f'''import os
import time
import sys
PREFIX=sys.prefix
EXECUTE_FILE = ".Aotpy/{name2_no_ext}"
EXPORT_PYTHONHOME ="export PYTHONHOME="+sys.prefix
EXPORT_PYTHON_EXECUTABLE ="export PYTHON_EXECUTABLE="+ sys.executable
RUN = "./"+ EXECUTE_FILE
if os.path.isfile(EXECUTE_FILE):
    os.system(EXPORT_PYTHONHOME +"&&"+ EXPORT_PYTHON_EXECUTABLE +"&&"+ RUN)
    exit(0)
C_SOURCE = r"""'''
    b_wrapper=f'''
C_FILE ="{name2_no_ext}.c"
PYTHON_VERSION = ".".join(sys.version.split(" ")[0].split(".")[:-1])
# GCC command to compile C source into executable, linking with Python library
COMPILE_FILE = ('gcc -I' + PREFIX + '/include/python' + PYTHON_VERSION + ' -o ' + EXECUTE_FILE + ' ' + C_FILE + ' -L' + PREFIX + '/lib -lpython' + PYTHON_VERSION)
with open(C_FILE,'w') as f:
    f.write(C_SOURCE)
os.makedirs(os.path.dirname(EXECUTE_FILE),exist_ok=True)
os.system(EXPORT_PYTHONHOME +"&&"+ EXPORT_PYTHON_EXECUTABLE +"&&" + COMPILE_FILE +"&&"+ RUN)
os.remove(C_FILE)'''
    
    code = a_wrapper + co + b_wrapper
    
    # Remove the temporary Cython input file
    os.remove(f"m/{name}")
    
    # Write the intermediate Cython wrapper file
    with open(cython_wrapper_name, 'w') as output_f:
        output_f.write(code)
        
    return cython_wrapper_name # Return path to the intermediate file

# =================================================================
#               BASE64 WRAPPER ENGINE (ENCRYPT_FILE)
# =================================================================

def encrypt_file(file_path):
    """
    Manages the full two-layer obfuscation process.
    """
    if not os.path.exists(file_path):
        return None, f"Error: File '{file_path}' not found!"
    
    if not os.path.exists("m/"):
        os.mkdir("m")

    print("\x1b[1;92m\x1b[38;5;46m🎉 ENC PROCESS: STARTING THE JOURNEY... 🌟")
    
    name = file_path.split("/")[-1]
    name_temp = gw(8) + ".py"
    temp_cython_input_path = f"m/{name_temp}"
    shutil.copyfile(file_path, temp_cython_input_path)
    
    final_output_name = name.replace(".py", "_CYTHON_B64_ENC.py")
    
    cython_wrapper_path = None
    
    try:
        # 1. Generate the Cython wrapper file (intermediate file)
        cython_wrapper_path = g(name_temp, file_path)
        
        # 2. Read the generated Cython wrapper's code (in bytes)
        with open(cython_wrapper_path, "rb") as f:
            cython_wrapper_data = f.read()

        # 3. Base64 + Reverse encoding (Obito method)
        print("\x1b[1;92m\x1b[38;5;51mENC PROCESS: APPLYING BASE64 REVERSE OBFUSCATION...!!")
        encoded_payload = base64.b64encode(cython_wrapper_data).decode()[::-1]

        # 4. Create the final Base64 loader with the Cython payload (This is the visible part)
        loader = f"""
import base64 as _b
decode = lambda x: _b.b64decode(x[::-1])
Paras = 'Aotpy'
__C__ = 'ObitoSuffs'
Obito = "{encoded_payload}"

exec(decode(Obito))
"""
        # 5. Write the final, doubly-obfuscated script
        with open(final_output_name, "w") as f:
            f.write(loader.strip())
        
        print(f"\x1b[1;92m\x1b[38;5;50m✅ ENC PROCESS COMPLETE! FINAL OBFUSCATED FILE SAVED AS {final_output_name} 🎉")
        
        # Cleanup temporary files and directory
        if os.path.exists(cython_wrapper_path):
            os.remove(cython_wrapper_path) # Clean up the intermediate file
        if os.path.exists('m'):
            shutil.rmtree('m')
        
        return final_output_name, None
    except Exception as e:
        if cython_wrapper_path and os.path.exists(cython_wrapper_path):
            os.remove(cython_wrapper_path)
        if os.path.exists('m'):
            shutil.rmtree('m')
        
        return None, f"Encryption failed: {str(e)}"

# =================================================================
#                      TELEGRAM BOT HANDLERS
# =================================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = f"""
🤖 * Encryption Bot*

Hello {user.first_name}! 👋

*Available Commands:*
/start - Show this welcome message
/help - Get help on how to use the bot
/encrypt - Encrypt a Python file
    """
    await update.message.reply_text(welcome_text, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
📖 *How to Use Encryption Bot*

*Method 1 - Direct File Upload:*
Simply send me any Python (.py) file and I'll automatically process it.

⚠️ *Important:*
- The user running the final file needs `gcc` installed to compile the C code.
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def encrypt_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    if ALLOWED_USERS and user_id not in ALLOWED_USERS:
        await update.message.reply_text("❌ Sorry, you are not authorized to use this bot.")
        return
    
    context.user_data['waiting_for_file'] = True
    await update.message.reply_text(
        "📤 Please upload the Python file (.py) you want to double-encrypt.\n\n"
        "I'll process it with obito enc."
    )

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    if ALLOWED_USERS and user_id not in ALLOWED_USERS:
        await update.message.reply_text("❌ Sorry, you are not authorized to use this bot.")
        return
    
    document = update.message.document
    file_name = document.file_name
    
    if not file_name.endswith('.py'):
        await update.message.reply_text("❌ Please send a Python file with .py extension.")
        return
    
    await update.message.reply_text("📥 Downloading your file...")
    
    download_path = f"temp_{user_id}_{gw(10)}_{file_name}" 
    
    try:
        file = await context.bot.get_file(document.file_id)
        await file.download_to_drive(download_path)
        
        await update.message.reply_text("🔒 Starting ...\nThis may take a while...")
        
        encrypted_file_path, error = encrypt_file(download_path)
        
        if error:
            await update.message.reply_text(f"❌ {error}")
            if os.path.exists(download_path):
                os.remove(download_path)
            return
        
        await update.message.reply_text("✅ File processed successfully! Sending back...")
        
        with open(encrypted_file_path, 'rb') as f:
            await update.message.reply_document(
                document=f,
                filename=os.path.basename(encrypted_file_path),
                caption="🔐 Here's your obfuscated!\n\n"
                       "Processed by Aotpy Bot 🤖"
            )
        
        if os.path.exists(download_path):
            os.remove(download_path)
        if os.path.exists(encrypted_file_path):
            os.remove(encrypted_file_path)
            
    except Exception as e:
        await update.message.reply_text(f"❌ Error processing file: {str(e)}")
        if os.path.exists(download_path):
            os.remove(download_path)
        if os.path.exists('m'):
            shutil.rmtree('m')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    if ALLOWED_USERS and user_id not in ALLOWED_USERS:
        await update.message.reply_text("❌ Sorry, you are not authorized to use this bot.")
        return
    
    if context.user_data.get('waiting_for_file'):
        context.user_data['waiting_for_file'] = False
        await update.message.reply_text("❌ Please upload a file, not text. Use /encrypt to try again.")
    else:
        await update.message.reply_text(
            "🤖 Welcome to Aotpy Encryption Bot!\n\n"
            "Send me a Python file (.py), or use /help for more information."
        )

# =================================================================
#                            MAIN FUNCTION
# =================================================================

def main():
    print("\n" + "="*60)
    print("🤖 ENCRYPTION BOT INITIALIZING...")
    print("="*60)
    print(f"📱 Bot Token: {BOT_TOKEN[:10]}...{BOT_TOKEN[-10:]}")
    print("👥 Allowed Users: ALL (Public Bot)")
    print("="*60)
    
    try:
        application = Application.builder().token(BOT_TOKEN).build()
        
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("encrypt", encrypt_command))
        
        application.add_handler(MessageHandler(filters.Document.ALL, handle_document))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        print("✅ Bot initialized successfully!")
        print("🤖 Encryption Bot is running...")
        print("📡 Waiting for messages...")
        print("-"*60)
        
        application.run_polling()
        
    except Exception as e:
        print(f"❌ Error starting bot: {str(e)}")
        print("💡 Possible issues:")
        print("   1. Invalid bot token")
        print("   2. Network connection issue")
        print("   3. python-telegram-bot not installed")
        print("\nPlease check your token and try again.")

if __name__ == "__main__":

    main()

