"use strict";
(self["webpackChunksingle_old"] = self["webpackChunksingle_old"] || []).push([
  [653],
  {
    7756: function (e, t, s) {
      (s.r(t),
        s.d(t, {
          default: function () {
            return Ae;
          },
        }));
      var i = function () {
          var e = this,
            t = e._self._c;
          return t(
            "div",
            {
              staticClass: "visualDetails",
              staticStyle: { "user-select": "none" },
            },
            [
              t("div", { staticClass: "visualDetails-inner" }, [
                t("div", { staticClass: "visualDetails-title" }, [
                  t(
                    "div",
                    { staticClass: "title-left", on: { click: e.goBack } },
                    [
                      t("el-image", { attrs: { src: e.downs } }),
                      t("div", { staticClass: "titles" }, [
                        e._v(e._s(e.visualProgramRow.name)),
                      ]),
                    ],
                    1,
                  ),
                  e._m(0),
                  t("div", { staticClass: "title-right" }),
                ]),
                t(
                  "div",
                  {
                    staticClass: "visualDetails-main",
                    attrs: { id: "visualDetailsMain" },
                  },
                  [
                    t("div", { staticClass: "container" }, [
                      t(
                        "div",
                        {
                          staticClass: "diagramExample",
                          on: {
                            mousedown: function (t) {
                              return e.startNodesBus(t);
                            },
                            mousemove: function (t) {
                              return e.moveNodesBus(t);
                            },
                            mouseup: function (t) {
                              return e.endNodesBus(t);
                            },
                          },
                        },
                        [
                          t("div", { staticClass: "left-div-style" }, [
                            t("div", {
                              ref: "pseudoDomLeft",
                              staticClass: "pseudo",
                            }),
                            t(
                              "div",
                              { staticClass: "left-style-bottom" },
                              e._l(e.initNodesBasic, function (s, i) {
                                return t("div", { key: i }, [
                                  "Object" == s.type
                                    ? t(
                                        "div",
                                        [
                                          "Module" == s.type
                                            ? t(
                                                "el-tooltip",
                                                {
                                                  staticClass: "item",
                                                  attrs: {
                                                    effect: "dark",
                                                    placement: "right",
                                                  },
                                                },
                                                [
                                                  t(
                                                    "div",
                                                    {
                                                      attrs: {
                                                        slot: "content",
                                                      },
                                                      slot: "content",
                                                    },
                                                    [
                                                      e._v(
                                                        " 名称：" +
                                                          e._s(s.fun) +
                                                          " ",
                                                      ),
                                                      t("br"),
                                                      t(
                                                        "div",
                                                        {
                                                          staticStyle: {
                                                            width: "200px",
                                                          },
                                                        },
                                                        [
                                                          e._v(
                                                            " 描述说明：" +
                                                              e._s(
                                                                s.description,
                                                              ) +
                                                              " ",
                                                          ),
                                                        ],
                                                      ),
                                                    ],
                                                  ),
                                                  e._l(
                                                    s.params,
                                                    function (i, a) {
                                                      return t(
                                                        "div",
                                                        {
                                                          key:
                                                            "nodes_basic" + a,
                                                          staticClass:
                                                            "basic-node",
                                                          on: {
                                                            mousedown:
                                                              function (t) {
                                                                return e.dragIt(
                                                                  s,
                                                                );
                                                              },
                                                          },
                                                        },
                                                        [
                                                          e._v(
                                                            " " +
                                                              e._s(i.fun) +
                                                              " ",
                                                          ),
                                                        ],
                                                      );
                                                    },
                                                  ),
                                                ],
                                                2,
                                              )
                                            : e._e(),
                                        ],
                                        1,
                                      )
                                    : t(
                                        "div",
                                        [
                                          t(
                                            "el-collapse",
                                            {
                                              staticClass: "titlecenter",
                                              attrs: { accordion: "" },
                                              model: {
                                                value: e.activeName,
                                                callback: function (t) {
                                                  e.activeName = t;
                                                },
                                                expression: "activeName",
                                              },
                                            },
                                            [
                                              t(
                                                "el-collapse-item",
                                                [
                                                  t(
                                                    "template",
                                                    { slot: "title" },
                                                    [
                                                      t("el-image", {
                                                        staticClass: "img1",
                                                        attrs: {
                                                          src: e.folter,
                                                        },
                                                      }),
                                                      t("span", [
                                                        e._v(
                                                          e._s(s.external_name),
                                                        ),
                                                      ]),
                                                    ],
                                                    1,
                                                  ),
                                                  e._l(s.spec, function (s, i) {
                                                    return t(
                                                      "div",
                                                      {
                                                        key: "nodes_basic" + i,
                                                      },
                                                      [
                                                        "Object" == s.type
                                                          ? t(
                                                              "el-tooltip",
                                                              {
                                                                staticClass:
                                                                  "item",
                                                                attrs: {
                                                                  effect:
                                                                    "dark",
                                                                  placement:
                                                                    "right",
                                                                },
                                                              },
                                                              [
                                                                t(
                                                                  "div",
                                                                  {
                                                                    attrs: {
                                                                      slot: "content",
                                                                    },
                                                                    slot: "content",
                                                                  },
                                                                  [
                                                                    e._v(
                                                                      " 名称：" +
                                                                        e._s(
                                                                          s.external_name,
                                                                        ) +
                                                                        " ",
                                                                    ),
                                                                    t("br"),
                                                                    t(
                                                                      "div",
                                                                      {
                                                                        staticStyle:
                                                                          {
                                                                            width:
                                                                              "400px",
                                                                          },
                                                                      },
                                                                      [
                                                                        e._v(
                                                                          " 描述说明：" +
                                                                            e._s(
                                                                              s.description,
                                                                            ) +
                                                                            " ",
                                                                        ),
                                                                      ],
                                                                    ),
                                                                  ],
                                                                ),
                                                                t(
                                                                  "div",
                                                                  {
                                                                    staticClass:
                                                                      "basic-node",
                                                                  },
                                                                  [
                                                                    t(
                                                                      "div",
                                                                      {
                                                                        staticClass:
                                                                          "over1",
                                                                      },
                                                                      [
                                                                        t(
                                                                          "el-image",
                                                                          {
                                                                            attrs:
                                                                              {
                                                                                src: e.file,
                                                                              },
                                                                          },
                                                                        ),
                                                                        t(
                                                                          "span",
                                                                          {
                                                                            staticClass:
                                                                              "cu1",
                                                                            on: {
                                                                              mousedown:
                                                                                function (
                                                                                  t,
                                                                                ) {
                                                                                  return e.dragIt(
                                                                                    s,
                                                                                  );
                                                                                },
                                                                            },
                                                                          },
                                                                          [
                                                                            e._v(
                                                                              e._s(
                                                                                s.external_name,
                                                                              ),
                                                                            ),
                                                                          ],
                                                                        ),
                                                                      ],
                                                                      1,
                                                                    ),
                                                                  ],
                                                                ),
                                                              ],
                                                            )
                                                          : t(
                                                              "div",
                                                              [
                                                                t(
                                                                  "el-collapse",
                                                                  {
                                                                    staticClass:
                                                                      "titlecenter",
                                                                    attrs: {
                                                                      accordion:
                                                                        "",
                                                                    },
                                                                  },
                                                                  [
                                                                    t(
                                                                      "el-collapse-item",
                                                                      [
                                                                        t(
                                                                          "template",
                                                                          {
                                                                            slot: "title",
                                                                          },
                                                                          [
                                                                            t(
                                                                              "el-image",
                                                                              {
                                                                                staticClass:
                                                                                  "img1",
                                                                                attrs:
                                                                                  {
                                                                                    src: e.folter,
                                                                                  },
                                                                              },
                                                                            ),
                                                                            t(
                                                                              "span",
                                                                              [
                                                                                e._v(
                                                                                  e._s(
                                                                                    s.external_name,
                                                                                  ),
                                                                                ),
                                                                              ],
                                                                            ),
                                                                          ],
                                                                          1,
                                                                        ),
                                                                        e._l(
                                                                          s.spec,
                                                                          function (
                                                                            s,
                                                                            i,
                                                                          ) {
                                                                            return t(
                                                                              "div",
                                                                              {
                                                                                key:
                                                                                  "nodes_basic" +
                                                                                  i,
                                                                              },
                                                                              [
                                                                                "Object" ==
                                                                                s.type
                                                                                  ? t(
                                                                                      "el-tooltip",
                                                                                      {
                                                                                        staticClass:
                                                                                          "item",
                                                                                        attrs:
                                                                                          {
                                                                                            effect:
                                                                                              "dark",
                                                                                            placement:
                                                                                              "right",
                                                                                          },
                                                                                      },
                                                                                      [
                                                                                        t(
                                                                                          "div",
                                                                                          {
                                                                                            attrs:
                                                                                              {
                                                                                                slot: "content",
                                                                                              },
                                                                                            slot: "content",
                                                                                          },
                                                                                          [
                                                                                            e._v(
                                                                                              " 名称：" +
                                                                                                e._s(
                                                                                                  s.external_name,
                                                                                                ) +
                                                                                                " ",
                                                                                            ),
                                                                                            t(
                                                                                              "br",
                                                                                            ),
                                                                                            t(
                                                                                              "div",
                                                                                              {
                                                                                                staticStyle:
                                                                                                  {
                                                                                                    width:
                                                                                                      "200px",
                                                                                                  },
                                                                                              },
                                                                                              [
                                                                                                e._v(
                                                                                                  " 描述说明：" +
                                                                                                    e._s(
                                                                                                      s.description,
                                                                                                    ) +
                                                                                                    " ",
                                                                                                ),
                                                                                              ],
                                                                                            ),
                                                                                          ],
                                                                                        ),
                                                                                        t(
                                                                                          "div",
                                                                                          {
                                                                                            staticClass:
                                                                                              "basic-node",
                                                                                          },
                                                                                          [
                                                                                            t(
                                                                                              "div",
                                                                                              {
                                                                                                staticClass:
                                                                                                  "over1",
                                                                                              },
                                                                                              [
                                                                                                t(
                                                                                                  "el-image",
                                                                                                  {
                                                                                                    attrs:
                                                                                                      {
                                                                                                        src: e.file,
                                                                                                      },
                                                                                                  },
                                                                                                ),
                                                                                                t(
                                                                                                  "span",
                                                                                                  {
                                                                                                    staticClass:
                                                                                                      "cu1",
                                                                                                    on: {
                                                                                                      mousedown:
                                                                                                        function (
                                                                                                          t,
                                                                                                        ) {
                                                                                                          return e.dragIt(
                                                                                                            s,
                                                                                                          );
                                                                                                        },
                                                                                                    },
                                                                                                  },
                                                                                                  [
                                                                                                    e._v(
                                                                                                      e._s(
                                                                                                        s.external_name,
                                                                                                      ),
                                                                                                    ),
                                                                                                  ],
                                                                                                ),
                                                                                              ],
                                                                                              1,
                                                                                            ),
                                                                                          ],
                                                                                        ),
                                                                                      ],
                                                                                    )
                                                                                  : e._e(),
                                                                              ],
                                                                              1,
                                                                            );
                                                                          },
                                                                        ),
                                                                      ],
                                                                      2,
                                                                    ),
                                                                  ],
                                                                  1,
                                                                ),
                                                              ],
                                                              1,
                                                            ),
                                                      ],
                                                      1,
                                                    );
                                                  }),
                                                ],
                                                2,
                                              ),
                                            ],
                                            1,
                                          ),
                                        ],
                                        1,
                                      ),
                                ]);
                              }),
                              0,
                            ),
                          ]),
                          t("DAGBoard", {
                            attrs: {
                              DataAll: e.yourJSONDataFillThere,
                              changeSizeNumber: e.changeSizeNumber,
                              alimentCenterData: e.alimentCenterData,
                            },
                            on: {
                              updateDAG: e.updateDAG,
                              editNodeDetails: e.editNodeDetails,
                              doSthPersonal: e.doSthPersonal,
                            },
                          }),
                          e.dragBus
                            ? t("node-bus", {
                                attrs: {
                                  value: e.busValue.value,
                                  pos_x: e.busValue.pos_x,
                                  pos_y: e.busValue.pos_y,
                                },
                              })
                            : e._e(),
                          t("div", { staticClass: "right-div-style" }, [
                            t("div", {
                              ref: "pseudoDomRight",
                              staticClass: "pseudo",
                            }),
                            t("h3", [e._v("模型参数")]),
                            e.formRowList.length
                              ? t(
                                  "ul",
                                  { staticClass: "module-container" },
                                  e._l(e.formRowList, function (s, i) {
                                    return t(
                                      "li",
                                      { key: i, staticClass: "li1" },
                                      [
                                        t(
                                          "div",
                                          { staticClass: "module-header" },
                                          [
                                            [
                                              t(
                                                "span",
                                                { staticClass: "header-name" },
                                                [e._v(e._s(s.internal_name))],
                                              ),
                                              t(
                                                "el-tooltip",
                                                {
                                                  attrs: {
                                                    placement: "bottom",
                                                    effect: "light",
                                                  },
                                                },
                                                [
                                                  t(
                                                    "div",
                                                    {
                                                      attrs: {
                                                        slot: "content",
                                                      },
                                                      slot: "content",
                                                    },
                                                    [
                                                      t("h4", [e._v("说明")]),
                                                      t(
                                                        "div",
                                                        {
                                                          staticStyle: {
                                                            "margin-top": "5px",
                                                          },
                                                        },
                                                        [
                                                          e._v(
                                                            " " +
                                                              e._s(
                                                                s.description,
                                                              ) +
                                                              " ",
                                                          ),
                                                        ],
                                                      ),
                                                    ],
                                                  ),
                                                  t("el-image", {
                                                    staticStyle: {
                                                      position: "relative",
                                                      top: "7px",
                                                      left: "6px",
                                                    },
                                                    attrs: { src: e.iconImg },
                                                  }),
                                                ],
                                                1,
                                              ),
                                            ],
                                          ],
                                          2,
                                        ),
                                        s.input_array.length > 1
                                          ? t(
                                              "div",
                                              {
                                                staticStyle: {
                                                  padding: "0 10px",
                                                  "margin-top": "10px",
                                                },
                                              },
                                              [
                                                t(
                                                  "el-select",
                                                  {
                                                    staticStyle: {
                                                      width: "100%",
                                                    },
                                                    attrs: {
                                                      placeholder:
                                                        "选择需要填写字段",
                                                      size: "small",
                                                    },
                                                    model: {
                                                      value: s.selfChoice,
                                                      callback: function (t) {
                                                        e.$set(
                                                          s,
                                                          "selfChoice",
                                                          t,
                                                        );
                                                      },
                                                      expression:
                                                        "item.selfChoice",
                                                    },
                                                  },
                                                  e._l(
                                                    s.input_array,
                                                    function (e) {
                                                      return t("el-option", {
                                                        key: e.input_type,
                                                        attrs: {
                                                          label: e.input_type,
                                                          value: e.input_type,
                                                        },
                                                      });
                                                    },
                                                  ),
                                                  1,
                                                ),
                                              ],
                                              1,
                                            )
                                          : e._e(),
                                        t(
                                          "div",
                                          { staticClass: "place-input" },
                                          e._l(s.input_array, function (i, a) {
                                            return t("div", { key: a }, [
                                              s.input_array.length > 1
                                                ? t(
                                                    "div",
                                                    [
                                                      "user_filepath" ===
                                                        i.input_type &&
                                                      "user_filepath" ===
                                                        s.selfChoice
                                                        ? t("el-input", {
                                                            attrs: {
                                                              size: "small",
                                                              placeholder:
                                                                "用户路径",
                                                            },
                                                            model: {
                                                              value: i.result3,
                                                              callback:
                                                                function (t) {
                                                                  e.$set(
                                                                    i,
                                                                    "result3",
                                                                    t,
                                                                  );
                                                                },
                                                              expression:
                                                                "inner.result3",
                                                            },
                                                          })
                                                        : e._e(),
                                                      ("single_choice" !==
                                                        i.input_type &&
                                                        "single_choice_object" !==
                                                          i.input_type &&
                                                        "boolean" !==
                                                          i.input_type) ||
                                                      ("single_choice" !==
                                                        s.selfChoice &&
                                                        "single_choice_object" !==
                                                          s.selfChoice &&
                                                        "boolean" !==
                                                          s.selfChoice)
                                                        ? e._e()
                                                        : t(
                                                            "div",
                                                            {
                                                              staticClass:
                                                                "choice",
                                                            },
                                                            [
                                                              t(
                                                                "div",
                                                                {
                                                                  staticClass:
                                                                    "radio",
                                                                },
                                                                [
                                                                  t(
                                                                    "el-radio-group",
                                                                    {
                                                                      model: {
                                                                        value:
                                                                          i.default0,
                                                                        callback:
                                                                          function (
                                                                            t,
                                                                          ) {
                                                                            e.$set(
                                                                              i,
                                                                              "default0",
                                                                              t,
                                                                            );
                                                                          },
                                                                        expression:
                                                                          "inner.default0",
                                                                      },
                                                                    },
                                                                    e._l(
                                                                      i.values,
                                                                      function (
                                                                        s,
                                                                        i,
                                                                      ) {
                                                                        return t(
                                                                          "el-radio",
                                                                          {
                                                                            key: i,
                                                                            attrs:
                                                                              {
                                                                                label:
                                                                                  s,
                                                                              },
                                                                          },
                                                                          [
                                                                            e._v(
                                                                              e._s(
                                                                                s,
                                                                              ),
                                                                            ),
                                                                          ],
                                                                        );
                                                                      },
                                                                    ),
                                                                    1,
                                                                  ),
                                                                ],
                                                                1,
                                                              ),
                                                            ],
                                                          ),
                                                      "multiple_choice" ===
                                                      i.input_type
                                                        ? t(
                                                            "div",
                                                            {
                                                              staticClass:
                                                                "choice",
                                                            },
                                                            [
                                                              t(
                                                                "div",
                                                                {
                                                                  staticClass:
                                                                    "radio",
                                                                },
                                                                [
                                                                  t(
                                                                    "el-checkbox-group",
                                                                    {
                                                                      model: {
                                                                        value:
                                                                          i.conditions,
                                                                        callback:
                                                                          function (
                                                                            t,
                                                                          ) {
                                                                            e.$set(
                                                                              i,
                                                                              "conditions",
                                                                              t,
                                                                            );
                                                                          },
                                                                        expression:
                                                                          "inner.conditions",
                                                                      },
                                                                    },
                                                                    e._l(
                                                                      i.values,
                                                                      function (
                                                                        s,
                                                                        i,
                                                                      ) {
                                                                        return t(
                                                                          "el-checkbox",
                                                                          {
                                                                            key: i,
                                                                            attrs:
                                                                              {
                                                                                label:
                                                                                  s,
                                                                              },
                                                                          },
                                                                          [
                                                                            e._v(
                                                                              e._s(
                                                                                s,
                                                                              ),
                                                                            ),
                                                                          ],
                                                                        );
                                                                      },
                                                                    ),
                                                                    1,
                                                                  ),
                                                                ],
                                                                1,
                                                              ),
                                                            ],
                                                          )
                                                        : e._e(),
                                                      "int" === i.input_type &&
                                                      "int" === s.selfChoice
                                                        ? t("el-input-number", {
                                                            staticStyle: {
                                                              width: "100%",
                                                            },
                                                            attrs: {
                                                              size: "small",
                                                              controls: !1,
                                                              placeholder:
                                                                "整数",
                                                              precision: 0,
                                                            },
                                                            on: {
                                                              blur: function (
                                                                t,
                                                              ) {
                                                                return e.integerBlur(
                                                                  t,
                                                                  i,
                                                                );
                                                              },
                                                            },
                                                            model: {
                                                              value: i.result,
                                                              callback:
                                                                function (t) {
                                                                  e.$set(
                                                                    i,
                                                                    "result",
                                                                    t,
                                                                  );
                                                                },
                                                              expression:
                                                                "inner.result",
                                                            },
                                                          })
                                                        : e._e(),
                                                      "float" ===
                                                        i.input_type &&
                                                      "float" === s.selfChoice
                                                        ? t("el-input-number", {
                                                            staticStyle: {
                                                              width: "100%",
                                                            },
                                                            attrs: {
                                                              size: "small",
                                                              controls: !1,
                                                              placeholder:
                                                                "浮点数",
                                                            },
                                                            on: {
                                                              blur: function (
                                                                t,
                                                              ) {
                                                                return e.floatBlur(
                                                                  t,
                                                                  i,
                                                                );
                                                              },
                                                            },
                                                            model: {
                                                              value: i.result2,
                                                              callback:
                                                                function (t) {
                                                                  e.$set(
                                                                    i,
                                                                    "result2",
                                                                    t,
                                                                  );
                                                                },
                                                              expression:
                                                                "inner.result2",
                                                            },
                                                          })
                                                        : e._e(),
                                                      "str" === i.input_type &&
                                                      "str" === s.selfChoice
                                                        ? t("el-input", {
                                                            attrs: {
                                                              size: "small",
                                                              placeholder:
                                                                "字符串",
                                                            },
                                                            model: {
                                                              value: i.result4,
                                                              callback:
                                                                function (t) {
                                                                  e.$set(
                                                                    i,
                                                                    "result4",
                                                                    t,
                                                                  );
                                                                },
                                                              expression:
                                                                "inner.result4",
                                                            },
                                                          })
                                                        : e._e(),
                                                      "url" === i.input_type &&
                                                      "url" === s.selfChoice
                                                        ? t("el-input", {
                                                            attrs: {
                                                              size: "small",
                                                              placeholder:
                                                                "url路径",
                                                            },
                                                            model: {
                                                              value: i.result5,
                                                              callback:
                                                                function (t) {
                                                                  e.$set(
                                                                    i,
                                                                    "result5",
                                                                    t,
                                                                  );
                                                                },
                                                              expression:
                                                                "inner.result5",
                                                            },
                                                          })
                                                        : e._e(),
                                                      "list" === i.input_type &&
                                                      "list" === s.selfChoice
                                                        ? t("el-input", {
                                                            attrs: {
                                                              size: "small",
                                                              placeholder:
                                                                "输入为：比如['1', '2']",
                                                            },
                                                            on: {
                                                              blur: function (
                                                                t,
                                                              ) {
                                                                return e.stringArrBlur(
                                                                  t,
                                                                  i,
                                                                );
                                                              },
                                                            },
                                                            model: {
                                                              value: i.result6,
                                                              callback:
                                                                function (t) {
                                                                  e.$set(
                                                                    i,
                                                                    "result6",
                                                                    t,
                                                                  );
                                                                },
                                                              expression:
                                                                "inner.result6",
                                                            },
                                                          })
                                                        : e._e(),
                                                      "tuple" ===
                                                        i.input_type &&
                                                      "tuple" === s.selfChoice
                                                        ? t("el-input", {
                                                            attrs: {
                                                              size: "small",
                                                              placeholder:
                                                                "输入为：比如(3,2)",
                                                            },
                                                            on: {
                                                              blur: e.yuanBlur,
                                                            },
                                                            model: {
                                                              value: i.result7,
                                                              callback:
                                                                function (t) {
                                                                  e.$set(
                                                                    i,
                                                                    "result7",
                                                                    t,
                                                                  );
                                                                },
                                                              expression:
                                                                "inner.result7",
                                                            },
                                                          })
                                                        : e._e(),
                                                    ],
                                                    1,
                                                  )
                                                : t(
                                                    "div",
                                                    [
                                                      "user_filepath" ===
                                                      i.input_type
                                                        ? t("el-input", {
                                                            attrs: {
                                                              size: "small",
                                                              placeholder:
                                                                "用户路径",
                                                            },
                                                            model: {
                                                              value: i.result3,
                                                              callback:
                                                                function (t) {
                                                                  e.$set(
                                                                    i,
                                                                    "result3",
                                                                    t,
                                                                  );
                                                                },
                                                              expression:
                                                                "inner.result3",
                                                            },
                                                          })
                                                        : e._e(),
                                                      "single_choice" ===
                                                        i.input_type ||
                                                      "single_choice_object" ===
                                                        i.input_type ||
                                                      "boolean" === i.input_type
                                                        ? t(
                                                            "div",
                                                            {
                                                              staticClass:
                                                                "choice",
                                                            },
                                                            [
                                                              t(
                                                                "div",
                                                                {
                                                                  staticClass:
                                                                    "radio",
                                                                },
                                                                [
                                                                  t(
                                                                    "el-radio-group",
                                                                    {
                                                                      model: {
                                                                        value:
                                                                          i.default0,
                                                                        callback:
                                                                          function (
                                                                            t,
                                                                          ) {
                                                                            e.$set(
                                                                              i,
                                                                              "default0",
                                                                              t,
                                                                            );
                                                                          },
                                                                        expression:
                                                                          "inner.default0",
                                                                      },
                                                                    },
                                                                    e._l(
                                                                      i.values,
                                                                      function (
                                                                        s,
                                                                        i,
                                                                      ) {
                                                                        return t(
                                                                          "el-radio",
                                                                          {
                                                                            key: i,
                                                                            attrs:
                                                                              {
                                                                                label:
                                                                                  s,
                                                                              },
                                                                          },
                                                                          [
                                                                            e._v(
                                                                              e._s(
                                                                                s,
                                                                              ),
                                                                            ),
                                                                          ],
                                                                        );
                                                                      },
                                                                    ),
                                                                    1,
                                                                  ),
                                                                ],
                                                                1,
                                                              ),
                                                            ],
                                                          )
                                                        : e._e(),
                                                      "multiple_choice" ===
                                                      i.input_type
                                                        ? t(
                                                            "div",
                                                            {
                                                              staticClass:
                                                                "choice",
                                                            },
                                                            [
                                                              t(
                                                                "div",
                                                                {
                                                                  staticClass:
                                                                    "radio",
                                                                },
                                                                [
                                                                  t(
                                                                    "el-checkbox-group",
                                                                    {
                                                                      model: {
                                                                        value:
                                                                          i.conditions,
                                                                        callback:
                                                                          function (
                                                                            t,
                                                                          ) {
                                                                            e.$set(
                                                                              i,
                                                                              "conditions",
                                                                              t,
                                                                            );
                                                                          },
                                                                        expression:
                                                                          "inner.conditions",
                                                                      },
                                                                    },
                                                                    e._l(
                                                                      i.values,
                                                                      function (
                                                                        s,
                                                                        i,
                                                                      ) {
                                                                        return t(
                                                                          "el-checkbox",
                                                                          {
                                                                            key: i,
                                                                            attrs:
                                                                              {
                                                                                label:
                                                                                  s,
                                                                              },
                                                                          },
                                                                          [
                                                                            e._v(
                                                                              e._s(
                                                                                s,
                                                                              ),
                                                                            ),
                                                                          ],
                                                                        );
                                                                      },
                                                                    ),
                                                                    1,
                                                                  ),
                                                                ],
                                                                1,
                                                              ),
                                                            ],
                                                          )
                                                        : e._e(),
                                                      "int" === i.input_type
                                                        ? t("el-input-number", {
                                                            staticStyle: {
                                                              width: "100%",
                                                            },
                                                            attrs: {
                                                              size: "small",
                                                              controls: !1,
                                                              placeholder:
                                                                "整数",
                                                              precision: 0,
                                                            },
                                                            on: {
                                                              blur: function (
                                                                t,
                                                              ) {
                                                                return e.integerBlur(
                                                                  t,
                                                                  i,
                                                                );
                                                              },
                                                            },
                                                            model: {
                                                              value: i.result,
                                                              callback:
                                                                function (t) {
                                                                  e.$set(
                                                                    i,
                                                                    "result",
                                                                    t,
                                                                  );
                                                                },
                                                              expression:
                                                                "inner.result",
                                                            },
                                                          })
                                                        : e._e(),
                                                      "float" === i.input_type
                                                        ? t("el-input-number", {
                                                            staticStyle: {
                                                              width: "100%",
                                                            },
                                                            attrs: {
                                                              size: "small",
                                                              controls: !1,
                                                              placeholder:
                                                                "浮点数",
                                                            },
                                                            on: {
                                                              blur: function (
                                                                t,
                                                              ) {
                                                                return e.floatBlur(
                                                                  t,
                                                                  i,
                                                                );
                                                              },
                                                            },
                                                            model: {
                                                              value: i.result2,
                                                              callback:
                                                                function (t) {
                                                                  e.$set(
                                                                    i,
                                                                    "result2",
                                                                    t,
                                                                  );
                                                                },
                                                              expression:
                                                                "inner.result2",
                                                            },
                                                          })
                                                        : e._e(),
                                                      "str" === i.input_type
                                                        ? t("el-input", {
                                                            attrs: {
                                                              size: "small",
                                                              placeholder:
                                                                "字符串",
                                                            },
                                                            model: {
                                                              value: i.result4,
                                                              callback:
                                                                function (t) {
                                                                  e.$set(
                                                                    i,
                                                                    "result4",
                                                                    t,
                                                                  );
                                                                },
                                                              expression:
                                                                "inner.result4",
                                                            },
                                                          })
                                                        : e._e(),
                                                      "url" === i.input_type
                                                        ? t("el-input", {
                                                            attrs: {
                                                              size: "small",
                                                              placeholder:
                                                                "url路径",
                                                            },
                                                            model: {
                                                              value: i.result5,
                                                              callback:
                                                                function (t) {
                                                                  e.$set(
                                                                    i,
                                                                    "result5",
                                                                    t,
                                                                  );
                                                                },
                                                              expression:
                                                                "inner.result5",
                                                            },
                                                          })
                                                        : e._e(),
                                                      "list" === i.input_type
                                                        ? t("el-input", {
                                                            attrs: {
                                                              size: "small",
                                                              placeholder:
                                                                "输入为：比如['1', '2']",
                                                            },
                                                            on: {
                                                              blur: function (
                                                                t,
                                                              ) {
                                                                return e.stringArrBlur(
                                                                  t,
                                                                  i,
                                                                );
                                                              },
                                                            },
                                                            model: {
                                                              value: i.result6,
                                                              callback:
                                                                function (t) {
                                                                  e.$set(
                                                                    i,
                                                                    "result6",
                                                                    t,
                                                                  );
                                                                },
                                                              expression:
                                                                "inner.result6",
                                                            },
                                                          })
                                                        : e._e(),
                                                      "tuple" === i.input_type
                                                        ? t("el-input", {
                                                            attrs: {
                                                              size: "small",
                                                              placeholder:
                                                                "输入为：比如(3,2)",
                                                            },
                                                            on: {
                                                              blur: e.yuanBlur,
                                                            },
                                                            model: {
                                                              value: i.result7,
                                                              callback:
                                                                function (t) {
                                                                  e.$set(
                                                                    i,
                                                                    "result7",
                                                                    t,
                                                                  );
                                                                },
                                                              expression:
                                                                "inner.result7",
                                                            },
                                                          })
                                                        : e._e(),
                                                    ],
                                                    1,
                                                  ),
                                            ]);
                                          }),
                                          0,
                                        ),
                                      ],
                                    );
                                  }),
                                  0,
                                )
                              : t(
                                  "div",
                                  { staticClass: "place-empty" },
                                  [
                                    t("el-image", { attrs: { src: e.empty } }),
                                    t("span", { staticClass: "empty-name" }, [
                                      e._v(
                                        "暂无参数，点击选中工作流节点后，在此处进行节点参数设置",
                                      ),
                                    ]),
                                  ],
                                  1,
                                ),
                          ]),
                        ],
                        1,
                      ),
                      t(
                        "div",
                        { staticClass: "option-top" },
                        [
                          t(
                            "div",
                            { staticClass: "option-left" },
                            [
                              t(
                                "el-select",
                                {
                                  attrs: { size: "small", clearable: "" },
                                  model: {
                                    value: e.openDir,
                                    callback: function (t) {
                                      e.openDir = t;
                                    },
                                    expression: "openDir",
                                  },
                                },
                                [
                                  t("el-option", {
                                    attrs: {
                                      label: "打开本地文件夹",
                                      value: "0",
                                    },
                                  }),
                                  t("el-option", {
                                    attrs: {
                                      label: "浏览历史记录",
                                      value: "1",
                                    },
                                  }),
                                ],
                                1,
                              ),
                            ],
                            1,
                          ),
                          t(
                            "div",
                            { staticClass: "option-right" },
                            [
                              t(
                                "el-select",
                                {
                                  attrs: { size: "small", clearable: "" },
                                  model: {
                                    value: e.createCodeToLocal,
                                    callback: function (t) {
                                      e.createCodeToLocal = t;
                                    },
                                    expression: "createCodeToLocal",
                                  },
                                },
                                [
                                  t("el-option", {
                                    attrs: {
                                      label: "生成代码到本地",
                                      value: "0",
                                    },
                                  }),
                                  t("el-option", {
                                    attrs: { label: "保存计算图", value: "1" },
                                  }),
                                  t("el-option", {
                                    attrs: {
                                      label: "生成代码并运行",
                                      value: "2",
                                    },
                                  }),
                                  t("el-option", {
                                    attrs: {
                                      label: "下载计算图图片",
                                      value: "3",
                                    },
                                  }),
                                ],
                                1,
                              ),
                            ],
                            1,
                          ),
                          t(
                            "el-button",
                            {
                              attrs: { size: "small", type: "success" },
                              on: { click: e.alimentCenter },
                            },
                            [e._v("居中")],
                          ),
                        ],
                        1,
                      ),
                      t(
                        "div",
                        { ref: "fixedRight", staticClass: "fix-right" },
                        [
                          t(
                            "div",
                            {
                              staticClass: "fix-right-item",
                              attrs: { title: "放大" },
                              on: {
                                click: function (t) {
                                  return e.sizeChange("+");
                                },
                              },
                            },
                            [t("el-image", { attrs: { src: e.enlarge } })],
                            1,
                          ),
                          t(
                            "div",
                            {
                              staticClass: "fix-right-item",
                              attrs: { title: "缩小" },
                              on: {
                                click: function (t) {
                                  return e.sizeChange("-");
                                },
                              },
                            },
                            [t("el-image", { attrs: { src: e.enlargeJian } })],
                            1,
                          ),
                          t(
                            "div",
                            {
                              staticClass: "fix-right-item",
                              attrs: { title: "退出全屏" },
                              on: {
                                click: function (t) {
                                  return e.sizeChange("exitFullScreen");
                                },
                              },
                            },
                            [t("el-image", { attrs: { src: e.huanyuan } })],
                            1,
                          ),
                          t(
                            "div",
                            {
                              staticClass: "fix-right-item",
                              attrs: { title: "恢复" },
                              on: {
                                click: function (t) {
                                  return e.sizeChange("init");
                                },
                              },
                            },
                            [t("el-image", { attrs: { src: e.jizhong } })],
                            1,
                          ),
                          t(
                            "div",
                            {
                              staticClass: "fix-right-item",
                              attrs: { title: "全屏" },
                              on: {
                                click: function (t) {
                                  return e.sizeChange("fullScreen");
                                },
                              },
                            },
                            [t("el-image", { attrs: { src: e.quanping } })],
                            1,
                          ),
                        ],
                      ),
                      t(
                        "div",
                        {
                          directives: [
                            {
                              name: "show",
                              rawName: "v-show",
                              value: e.resourceIsShow,
                              expression: "resourceIsShow",
                            },
                          ],
                          staticClass: "resource",
                        },
                        [
                          t("div", { staticClass: "resource-title" }, [
                            t(
                              "div",
                              {
                                staticClass: "resource-title-left",
                                on: { click: e.packUp },
                              },
                              [
                                t("el-image", { attrs: { src: e.shouqi } }),
                                t("span", { staticClass: "resource-name" }, [
                                  e._v("收起"),
                                ]),
                              ],
                              1,
                            ),
                            t(
                              "div",
                              {
                                staticClass: "resource-title-right",
                                on: { click: e.goDetail },
                              },
                              [
                                t("el-image", { attrs: { src: e.xiangyou } }),
                                t("span", { staticClass: "resource-name" }, [
                                  e._v("详情"),
                                ]),
                              ],
                              1,
                            ),
                          ]),
                          e._m(1),
                        ],
                      ),
                    ]),
                  ],
                ),
              ]),
            ],
          );
        },
        a = [
          function () {
            var e = this,
              t = e._self._c;
            return t("div", { staticClass: "title-middle" }, [
              t("div", { staticClass: "title-tab" }),
            ]);
          },
          function () {
            var e = this,
              t = e._self._c;
            return t("div", { staticClass: "resource-box" }, [
              t("div", { staticClass: "resource-item" }, [
                t("div", { staticClass: "resource-item-title" }, [
                  t("div", { staticClass: "resource-item-title-left" }, [
                    e._v("CPU使用率"),
                  ]),
                  t("div", { staticClass: "resource-item-title-right" }, [
                    e._v("25.5%"),
                  ]),
                ]),
                t("div", {
                  staticClass: "resource-item-container",
                  attrs: { id: "content-cpu" },
                }),
              ]),
              t("div", { staticClass: "resource-item" }, [
                t("div", { staticClass: "resource-item-title" }, [
                  t("div", { staticClass: "resource-item-title-left" }, [
                    e._v("GPU使用率"),
                  ]),
                  t("div", { staticClass: "resource-item-title-right" }, [
                    e._v("25.5%"),
                  ]),
                ]),
                t("div", {
                  staticClass: "resource-item-container",
                  attrs: { id: "content-gpu" },
                }),
              ]),
              t("div", { staticClass: "resource-item" }, [
                t("div", { staticClass: "resource-item-title" }, [
                  t("div", { staticClass: "resource-item-title-left" }, [
                    e._v("内存使用率"),
                  ]),
                  t("div", { staticClass: "resource-item-title-right" }, [
                    e._v("25.5%"),
                  ]),
                ]),
                t("div", {
                  staticClass: "resource-item-container",
                  attrs: { id: "content-storage" },
                }),
              ]),
            ]);
          },
        ],
        n = (s(4114), s(2225)),
        l = s(2865),
        o = s(8643),
        r = s(666),
        c = s(1022),
        u = s(1920),
        d = s(7933),
        h = s(8243),
        p = s(4834),
        g = s(9730),
        m = s(6552),
        _ = s(1229),
        v = s(191),
        f = s(7373),
        y = s(6454),
        x = s(3192),
        S = s(9002),
        b = s(5715),
        k = s(241),
        w = s(3732),
        C = function () {
          var e = this,
            t = e._self._c;
          return t(
            "svg",
            {
              style: {
                cursor:
                  "move_graph" === this.currentEvent ? "grabbing" : "grab",
              },
              attrs: {
                id: "svgContent",
                xmlns: "http://www.w3.org/2000/svg",
                "xmlns:xlink": "http://www.w3.org/1999/xlink",
                version: "1.1",
                width: "100%",
                height: "1029",
                "data-spm-anchor-id": "TODO.11007039.0.i6.12b64a9bcbXQmm",
              },
              on: {
                mousedown: e.svgMouseDown,
                mousemove: function (t) {
                  return e.dragIng(t);
                },
                mouseleave: e.atMouseOut,
                mouseup: function (t) {
                  return e.dragEnd(t);
                },
              },
            },
            [
              t(
                "g",
                {
                  attrs: {
                    transform: ` translate(${e.svg_left}, ${e.svg_top}) scale(${e.svgScale})`,
                  },
                },
                [
                  e._l(e.DataAll.nodes, function (s, i) {
                    return t(
                      "g",
                      {
                        key: "_" + i,
                        staticClass: "svgEach",
                        attrs: {
                          transform: `translate(${s.pos_x}, ${s.pos_y})`,
                        },
                        on: {
                          contextmenu: function (t) {
                            return e.r_click_nodes(t, i);
                          },
                          dblclick: function (t) {
                            return e.focusInput(t.path[0]);
                          },
                          mousedown: function (t) {
                            return e.dragPre(t, i, s);
                          },
                        },
                      },
                      [
                        t("main-body", {
                          attrs: {
                            item: s,
                            i: i,
                            choice: e.choice,
                            currentEvent: e.currentEvent,
                          },
                          on: {
                            nodesPersonalEvent: e.nodesPersonalEvent,
                            changeNodeName: e.changeNodeName,
                            linkEnd: e.linkEnd,
                            linkPre: e.linkPre,
                          },
                        }),
                      ],
                      1,
                    );
                  }),
                  e._l(e.DataAll.edges, function (s, i) {
                    return t("Arrow", {
                      key: "____" + i,
                      attrs: { DataAll: e.DataAll, each: s, index: i },
                      on: {
                        delEdge: e.delEdge,
                        close_click_nodes: e.close_click_nodes,
                      },
                    });
                  }),
                  "dragLink" === e.currentEvent
                    ? t("SimulateArrow", { attrs: { dragLink: e.dragLink } })
                    : e._e(),
                  -1 !== ["sel_area", "sel_area_ing"].indexOf(e.currentEvent)
                    ? t("SimulateSelArea", {
                        attrs: { simulate_sel_area: e.simulate_sel_area },
                      })
                    : e._e(),
                ],
                2,
              ),
              t("EditArea", {
                attrs: { isEditAreaShow: e.is_edit_area },
                on: {
                  editNodeDetails: e.editNodeDetails,
                  nodesPersonalEvent: e.nodesPersonalEvent,
                  delNode: e.delNode,
                  changePort: e.changePort,
                  close_click_nodes: e.close_click_nodes,
                },
              }),
              t("Control", {
                attrs: {
                  modelRunningStatus: e.modelRunningStatus,
                  currentEvent: e.currentEvent,
                },
                on: {
                  changeModelRunningStatus: e.changeModelRunningStatus,
                  sizeInit: e.sizeInit,
                  sizeExpend: e.sizeExpend,
                  sizeShrink: e.sizeShrink,
                  sel_area: e.sel_area,
                },
              }),
            ],
            1,
          );
        },
        $ = [],
        D = function () {
          var e = this,
            t = e._self._c;
          return this.DataAll
            ? t("g", [
                t("path", {
                  class:
                    e.isHover || e.r_click_menu
                      ? "connector-hl"
                      : e.each.type && "active" == e.each.type
                        ? "connector-active"
                        : e.each.type && "success" == e.each.type
                          ? "connector"
                          : "defaultArrow",
                  style: e.each.style,
                  attrs: { d: e.computedLink(), "stroke-dasharray": "20 2" },
                  on: {
                    mouseover: e.pathHover,
                    mouseout: e.pathOut,
                    contextmenu: function (t) {
                      return e.r_click(t);
                    },
                  },
                }),
                e.each.edgesText
                  ? t("text", { ref: "edgeText", style: e.computedText() }, [
                      e._v(e._s(e.each.edgesText)),
                    ])
                  : e._e(),
                t("polyline", {
                  staticClass: "only-watch-el",
                  staticStyle: { stroke: "#006600" },
                  attrs: { points: e.computedArrow() },
                }),
                t("circle", {
                  staticClass: "only-watch-el",
                  staticStyle: {
                    stroke: "#006600",
                    "stroke-width": "2",
                    fill: "#FFFFFF",
                  },
                  attrs: { cx: e.computedCx(), cy: e.computedCy(), r: "5" },
                }),
                e.r_click_menu
                  ? t("g", [
                      t(
                        "foreignObject",
                        {
                          staticStyle: { position: "relative" },
                          attrs: { width: "100%", height: "100%" },
                          on: {
                            click: function (t) {
                              return e.click_menu_cover(t);
                            },
                          },
                        },
                        [
                          t(
                            "body",
                            {
                              style: e.menu_style,
                              attrs: { xmlns: "http://www.w3.org/1999/xhtml" },
                            },
                            [
                              t("div", { staticClass: "menu_contain" }, [
                                t("span", { on: { click: e.delEdges } }, [
                                  e._v("删除"),
                                ]),
                              ]),
                            ],
                          ),
                        ],
                      ),
                    ])
                  : e._e(),
              ])
            : e._e();
        },
        N = [],
        A = {
          watch: {},
          props: {
            DataAll: { type: Object },
            each: { type: Object },
            index: { type: Number },
          },
          computed: {
            svgScale() {
              return sessionStorage["svgScale"] || 1;
            },
          },
          data() {
            return {
              isHover: !1,
              r_click_menu: !1,
              menu_style: { position: "absolute", left: "358px", top: "264px" },
            };
          },
          methods: {
            pathHover() {
              this.isHover = !0;
            },
            pathOut() {
              this.isHover = !1;
            },
            click_menu_cover(e) {
              (this.$emit("close_click_nodes"),
                (this.r_click_menu = !1),
                e.preventDefault(),
                (e.cancelBubble = !0),
                e.stopPropagation());
            },
            delEdges() {
              let e = { id: this.each.id };
              this.$emit("delEdge", e);
            },
            r_click(e) {
              console.log(this.svgScale);
              const t = e.offsetX,
                s = e.offsetY;
              ((this.menu_style = Object.assign({}, this.menu_style, {
                left:
                  (t - (sessionStorage["svg_left"] || 0)) / this.svgScale +
                  "px",
                top:
                  (s - (sessionStorage["svg_top"] || 0)) / this.svgScale + "px",
              })),
                (this.r_click_menu = !0),
                e.stopPropagation(),
                e.preventDefault(),
                (e.cancelBubble = !0));
            },
            computedLink() {
              let e, t, s, i;
              if (this.DataAll) {
                const {
                    dst_input_idx: a,
                    dst_node_id: n,
                    src_node_id: l,
                    src_output_idx: o,
                  } = this.each,
                  r = this.DataAll.nodes.find((e) => e.id === l),
                  c = this.DataAll.nodes.find((e) => e.id === n);
                return this.isVertical()
                  ? ((e = r.pos_x + (180 / (r.out_ports.length + 1)) * (o + 1)),
                    (t = r.pos_y + 30),
                    (s = c.pos_x + (180 / (c.in_ports.length + 1)) * (a + 1)),
                    (i = c.pos_y),
                    `M ${e} ${t}  Q ${e} ${t + 50} ${(s + e) / 2} ${(i + t) / 2} T ${s} ${i}`)
                  : ((e = r.pos_x + 180),
                    (t = r.pos_y + 15),
                    (s = c.pos_x),
                    (i = c.pos_y + 15),
                    `M ${e} ${t}  Q ${e + 30} ${t} ${(s + e) / 2} ${(i + t) / 2} T ${s} ${i}`);
              }
              return "M 0 0 T 0 0";
            },
            computedText() {
              if (this.DataAll) {
                const {
                    dst_input_idx: e,
                    dst_node_id: t,
                    src_node_id: s,
                    src_output_idx: i,
                  } = this.each,
                  a = this.DataAll.nodes.find((e) => e.id === s),
                  n = this.DataAll.nodes.find((e) => e.id === t),
                  l = a.pos_x + (180 / (a.out_ports.length + 1)) * (i + 1),
                  o = a.pos_y + 30,
                  r = n.pos_x + (180 / (n.in_ports.length + 1)) * (e + 1),
                  c = n.pos_y;
                return {
                  transform: `translate(${(l + r) / 2}px, ${(o + c) / 2}px)`,
                  stroke: "#fff",
                  ...this.each.textStyle,
                };
              }
              return "M 0 0 T 0 0";
            },
            computedArrow() {
              if (this.DataAll) {
                const {
                    dst_input_idx: e,
                    dst_node_id: t,
                    src_node_id: s,
                    src_output_idx: i,
                  } = this.each,
                  a = this.DataAll.nodes.find((e) => e.id === t);
                let n = a.pos_x + (180 / (a.in_ports.length + 1)) * (e + 1),
                  l = a.pos_y;
                if (this.isVertical())
                  return `${n} ${l + 3} ${n - 3} ${l - 3} ${n + 3} ${l - 3}`;
                {
                  let e = a.pos_x,
                    t = a.pos_y + 15;
                  return `${e - 2} ${t + 3} ${e - 3} ${t - 3} ${e + 3} ${t - 1}`;
                }
              }
              return "0,0 0,0 0,0";
            },
            computedCx() {
              const { src_node_id: e, src_output_idx: t } = this.each,
                s = this.DataAll.nodes.find((t) => t.id === e);
              let i = 0;
              return (
                (i = this.isVertical()
                  ? s.pos_x + (180 / (s.out_ports.length + 1)) * (t + 1)
                  : s.pos_x + 180),
                `${i}`
              );
            },
            computedCy() {
              let e = 0;
              const { src_node_id: t } = this.each,
                s = this.DataAll.nodes.find((e) => e.id === t);
              return (
                (e = this.isVertical() ? s.pos_y + 30 : s.pos_y + 15),
                `${e}`
              );
            },
            isVertical() {
              let e = { isVertical: !0 },
                t = localStorage.getItem("GlobalConfig");
              return (
                t && t.length > 0 && (e = Object.assign(e, JSON.parse(t))),
                e.isVertical
              );
            },
          },
          mounted() {
            this.$nextTick(() => {
              this.$refs.edgeText &&
                console.log(this.$refs.edgeText.style.width);
            });
          },
        },
        E = A,
        O = s(1656),
        P = (0, O.A)(E, D, N, !1, null, "75bbcf8d", null),
        z = P.exports,
        F = function () {
          var e = this,
            t = e._self._c;
          return t("g", [
            t("path", {
              staticClass: "connector only-watch-el",
              attrs: { d: e.dragLinkPath() },
            }),
            t("circle", {
              staticStyle: {
                stroke: "#006600",
                "stroke-width": "2",
                fill: "#CCCCCC",
              },
              attrs: {
                cx: this.dragLink.fromX,
                cy: this.dragLink.fromY,
                r: "5",
              },
            }),
            t("polyline", {
              staticClass: "only-watch-el",
              staticStyle: { stroke: "#006600" },
              attrs: { points: e.computedArrow() },
            }),
          ]);
        },
        I = [],
        B = {
          props: { dragLink: { type: Object } },
          methods: {
            dragLinkPath() {
              const { fromX: e, fromY: t, toX: s, toY: i } = this.dragLink;
              return this.isVertical()
                ? `M ${e} ${t}  Q ${e} ${t + 50} ${(s + e) / 2} ${(t + i) / 2} T ${s} ${i}`
                : `M ${e} ${t} Q ${e + 30} ${t}  ${(s + e) / 2} ${(t + i) / 2} T ${s} ${i}`;
            },
            computedArrow() {
              const { toX: e, toY: t } = this.dragLink;
              return this.isVertical()
                ? `${e} ${t} ${e - 3} ${t - 6} ${e + 3} ${t - 6}`
                : `${e - 3} ${t + 3} ${e} ${t} ${e - 3} ${t - 3}`;
            },
            isVertical() {
              let e = { isVertical: !0 },
                t = localStorage.getItem("GlobalConfig");
              return (
                t && t.length > 0 && (e = Object.assign(e, JSON.parse(t))),
                e.isVertical
              );
            },
          },
        },
        M = B,
        L = (0, O.A)(M, F, I, !1, null, "34953c3e", null),
        T = L.exports,
        R = function () {
          var e = this,
            t = e._self._c;
          return t(
            "g",
            {
              staticClass: "dragFrame",
              attrs: {
                transform: `translate(${e.dragFrame.posX}, ${e.dragFrame.posY})`,
              },
            },
            [
              t("foreignObject", { attrs: { width: "180", height: "30" } }, [
                t(
                  "body",
                  {
                    staticStyle: { margin: "0" },
                    attrs: { xmlns: "http://www.w3.org/1999/xhtml" },
                  },
                  [t("div", { staticClass: "dragFrameArea" })],
                ),
              ]),
            ],
          );
        },
        j = [],
        J = { props: { dragFrame: { type: Object } }, methods: {} },
        G = J,
        V = (0, O.A)(G, R, j, !1, null, "672c8096", null),
        X = V.exports,
        Y = function () {
          var e = this,
            t = e._self._c;
          return e.isEditAreaShow.value
            ? t("g", [
                t(
                  "foreignObject",
                  {
                    staticStyle: { position: "relative" },
                    attrs: { width: "100%", height: "100%" },
                    on: {
                      click: function (t) {
                        return e.click_menu_cover(t);
                      },
                    },
                  },
                  [
                    t(
                      "body",
                      {
                        style: e.get_menu_style(),
                        attrs: { xmlns: "http://www.w3.org/1999/xhtml" },
                      },
                      [
                        t(
                          "div",
                          { staticClass: "menu_contain" },
                          [
                            t("span", { on: { click: e.delEdges } }, [
                              e._v("删除"),
                            ]),
                            e.isEditAreaShow.detail
                              ? t("span", { on: { click: e.editNode } }, [
                                  e._v("EDIT IT"),
                                ])
                              : e._e(),
                            e._l(
                              e.isEditAreaShow.rightClickEvent,
                              function (s) {
                                return t(
                                  "span",
                                  {
                                    key: s.label,
                                    on: {
                                      click: function (t) {
                                        return e.handlePersonalThs(s.eventName);
                                      },
                                    },
                                  },
                                  [e._v(e._s(s.label))],
                                );
                              },
                            ),
                          ],
                          2,
                        ),
                      ],
                    ),
                  ],
                ),
              ])
            : e._e();
        },
        q = [],
        W = {
          props: {
            isEditAreaShow: {
              type: Object,
              default: () => ({ value: !1, x: -9999, y: -9999, id: null }),
            },
          },
          mounted() {
            console.log("isEditAreaShow", this.isEditAreaShow);
          },
          methods: {
            click_menu_cover(e) {
              (this.$emit("close_click_nodes"),
                e.preventDefault(),
                (e.cancelBubble = !0),
                e.stopPropagation());
            },
            get_menu_style() {
              let e = this.isEditAreaShow.x,
                t = this.isEditAreaShow.y;
              return { position: "absolute", left: e + "px", top: t + "px" };
            },
            delEdges() {
              let e = {
                model_id: sessionStorage["newGraph"],
                id: this.isEditAreaShow.id,
              };
              (this.$emit("delNode", e), this.$emit("close_click_nodes"));
            },
            changePort(e) {
              this.$emit("changePort", e, this.isEditAreaShow.id);
            },
            editNode() {
              this.$emit("editNodeDetails", this.isEditAreaShow);
            },
            handlePersonalThs(e) {
              this.$emit("nodesPersonalEvent", e, this.isEditAreaShow.id);
            },
          },
        },
        H = W,
        U = (0, O.A)(H, Y, q, !1, null, "263c0efc", null),
        Q = U.exports,
        K = function () {
          var e = this,
            t = e._self._c;
          return t("g", [
            t(
              "foreignObject",
              {
                staticStyle: { position: "relative", "line-height": "20px" },
                attrs: { width: "200px", height: "30px" },
              },
              [
                t(
                  "body",
                  { attrs: { xmlns: "http://www.w3.org/1999/xhtml" } },
                  [
                    t("div", { staticClass: "control_menu" }, [
                      t("span", { on: { click: e.sizeExpend } }, [
                        t(
                          "svg",
                          {
                            staticClass: "icon",
                            attrs: { "aria-hidden": "true" },
                          },
                          [
                            t("use", {
                              attrs: { "xlink:href": "#icon-fangda" },
                            }),
                          ],
                        ),
                      ]),
                      t("span", { on: { click: e.sizeShrink } }, [
                        t(
                          "svg",
                          {
                            staticClass: "icon",
                            attrs: { "aria-hidden": "true" },
                          },
                          [
                            t("use", {
                              attrs: { "xlink:href": "#icon-suoxiao" },
                            }),
                          ],
                        ),
                      ]),
                      t("span", { on: { click: e.sizeInit } }, [
                        t(
                          "svg",
                          {
                            staticClass: "icon",
                            attrs: { "aria-hidden": "true" },
                          },
                          [
                            t("use", {
                              attrs: { "xlink:href": "#icon-icon-test" },
                            }),
                          ],
                        ),
                      ]),
                      t(
                        "span",
                        {
                          class:
                            -1 !==
                            ["sel_area", "sel_area_ing"].indexOf(e.currentEvent)
                              ? "sel_ing"
                              : "",
                          on: {
                            click: function (t) {
                              return e.sel_area(t);
                            },
                          },
                        },
                        [
                          t(
                            "svg",
                            {
                              staticClass: "icon",
                              attrs: { "aria-hidden": "true" },
                            },
                            [
                              t("use", {
                                attrs: { "xlink:href": "#icon-duoxuankuang" },
                              }),
                            ],
                          ),
                        ],
                      ),
                      t("span", { on: { click: e.fullScreen } }, [
                        t(
                          "svg",
                          {
                            staticClass: "icon",
                            attrs: { "aria-hidden": "true" },
                          },
                          [
                            t("use", {
                              attrs: { "xlink:href": "#icon-quanping" },
                            }),
                          ],
                        ),
                      ]),
                    ]),
                  ],
                ),
              ],
            ),
          ]);
        },
        Z = [],
        ee = {
          props: {
            currentEvent: { type: String, default: () => {} },
            modelRunningStatus: { type: Boolean, default: () => !1 },
          },
          data() {
            return { changeScreen: "full" };
          },
          methods: {
            sizeExpend() {
              this.$emit("sizeExpend");
            },
            sizeShrink() {
              this.$emit("sizeShrink");
            },
            sizeInit() {
              this.$emit("sizeInit");
            },
            sel_area(e) {
              (this.$emit("sel_area"),
                e.preventDefault(),
                e.stopPropagation(),
                (e.cancelBubble = !0));
            },
            fullScreen() {
              if ("full" === this.changeScreen) {
                this.changeScreen = "mini";
                let e = document.getElementById("svgContent");
                e.webkitRequestFullScreen();
              } else
                ((this.changeScreen = "full"), document.webkitExitFullscreen());
            },
            changeModelRunningStatus() {
              this.$emit("changeModelRunningStatus", !this.modelRunningStatus);
            },
          },
        },
        te = ee,
        se = (0, O.A)(te, K, Z, !1, null, "1ea5f094", null),
        ie = se.exports,
        ae = function () {
          var e = this,
            t = e._self._c;
          return t("g", [
            t(
              "foreignObject",
              {
                staticStyle: { position: "abolute" },
                attrs: { width: "100%", height: "100%" },
              },
              [
                t("body", {
                  style: e.getSimulateSelArea(),
                  attrs: {
                    xmlns: "http://www.w3.org/1999/xhtml",
                    id: "simulate_sel_area",
                  },
                }),
              ],
            ),
          ]);
        },
        ne = [],
        le = {
          props: {
            simulate_sel_area: {
              type: Object,
              default: () => ({ left: 0, top: 0, width: 0, height: 0 }),
            },
          },
          methods: {
            getSimulateSelArea() {
              const {
                left: e,
                top: t,
                width: s,
                height: i,
              } = this.simulate_sel_area;
              return `width: ${s}px; height: ${i}px; left: ${e}px; top: ${t}px; border: 3px dashed #289de9;position: absolute;`;
            },
          },
        },
        oe = le,
        re = (0, O.A)(oe, ae, ne, !1, null, "906a5b26", null),
        ce = re.exports,
        ue = function () {
          var e = this,
            t = e._self._c;
          return e.isVertical()
            ? t("foreignObject", { attrs: { width: "180", height: "30" } }, [
                t(
                  "body",
                  {
                    staticStyle: { margin: "0" },
                    attrs: { xmlns: "http://www.w3.org/1999/xhtml" },
                  },
                  [
                    t("div", [
                      t(
                        "div",
                        {
                          class:
                            -1 !== e.choice.paneNode.indexOf(e.item.id)
                              ? "pane-node-content selected"
                              : "pane-node-content",
                          style: e.item.nodeStyle,
                        },
                        [
                          t("i", {
                            class: `${e.item.iconClassName || "el-icon-coin"} icon icon-data`,
                            style: e.item.iconStyle,
                            on: {
                              dblclick: function (t) {
                                return e.$emit(
                                  "nodesPersonalEvent",
                                  "dbClickNodeIcon",
                                  e.item.id,
                                );
                              },
                            },
                          }),
                          t("p", { staticClass: "name" }, [
                            e._v(e._s(e.item.name)),
                          ]),
                          t("p", {
                            staticClass: "finish el-icon-check",
                            on: {
                              mousedown: function (t) {
                                return (
                                  t.stopPropagation(),
                                  e.test.apply(null, arguments)
                                );
                              },
                            },
                          }),
                        ],
                      ),
                      -1 !== e.choice.paneNode.indexOf(e.item.id)
                        ? t("p", { staticClass: "node-pop" }, [
                            e._v(e._s(e.item.nameDescribe || e.item.name)),
                          ])
                        : e._e(),
                      t(
                        "div",
                        {
                          class:
                            "dragLink" === e.currentEvent
                              ? "pane-node-parent-hl"
                              : "pane-node-parent",
                        },
                        e._l(e.item.in_ports, function (s, i) {
                          return t(
                            "div",
                            {
                              key: "__" + i,
                              style: {
                                width: 100 / (e.item.in_ports.length + 1) + "%",
                              },
                            },
                            [
                              t("span", {
                                staticClass: "space",
                                on: {
                                  mouseup: function (t) {
                                    return e.$emit("linkEnd", e.i, i);
                                  },
                                },
                              }),
                            ],
                          );
                        }),
                        0,
                      ),
                      t(
                        "div",
                        { staticClass: "pane-node-children" },
                        e._l(e.item.out_ports, function (s, i) {
                          return t(
                            "div",
                            {
                              key: "___" + i,
                              style: {
                                width:
                                  100 / (e.item.out_ports.length + 1) + "%",
                              },
                            },
                            [
                              t("span", {
                                staticClass: "space",
                                on: {
                                  mousedown: function (t) {
                                    return e.$emit("linkPre", t, e.i, i);
                                  },
                                },
                              }),
                            ],
                          );
                        }),
                        0,
                      ),
                    ]),
                  ],
                ),
              ])
            : t("foreignObject", { attrs: { width: "180", height: "30" } }, [
                t(
                  "body",
                  {
                    staticStyle: { margin: "0" },
                    attrs: { xmlns: "http://www.w3.org/1999/xhtml" },
                  },
                  [
                    t("div", [
                      t(
                        "div",
                        {
                          class:
                            -1 !== e.choice.paneNode.indexOf(e.item.id)
                              ? "pane-node-content selected"
                              : "pane-node-content",
                          style: e.item.nodeStyle,
                        },
                        [
                          t("i", {
                            class: `${e.item.iconClassName || "el-icon-coin"} icon icon-data`,
                            style: e.item.iconStyle,
                            on: {
                              dblclick: function (t) {
                                return e.$emit(
                                  "nodesPersonalEvent",
                                  "dbClickNodeIcon",
                                  e.item.id,
                                );
                              },
                            },
                          }),
                          t("p", { staticClass: "name" }, [
                            e._v(e._s(e.item.name)),
                          ]),
                          t("p", { staticClass: "finish" }, [e._v("徐晓2")]),
                        ],
                      ),
                      -1 !== e.choice.paneNode.indexOf(e.item.id)
                        ? t("p", { staticClass: "node-pop" }, [
                            e._v(e._s(e.item.nameDescribe || e.item.name)),
                          ])
                        : e._e(),
                      t(
                        "div",
                        {
                          class:
                            "dragLink" === e.currentEvent
                              ? "pane-node-parent-hl"
                              : "pane-node-parent",
                          attrs: { id: "parent-cross" },
                        },
                        e._l(e.item.in_ports, function (s, i) {
                          return t(
                            "div",
                            {
                              key: "__" + i,
                              style: {
                                width: 100 / (e.item.in_ports.length + 1) + "%",
                              },
                            },
                            [
                              t("span", {
                                staticClass: "space",
                                on: {
                                  mouseup: function (t) {
                                    return e.$emit("linkEnd", e.i, i);
                                  },
                                },
                              }),
                            ],
                          );
                        }),
                        0,
                      ),
                      t(
                        "div",
                        {
                          staticClass: "pane-node-children",
                          attrs: { id: "children-cross" },
                        },
                        e._l(e.item.out_ports, function (s, i) {
                          return t(
                            "div",
                            {
                              key: "___" + i,
                              style: {
                                width:
                                  100 / (e.item.out_ports.length + 1) + "%",
                              },
                            },
                            [
                              t("span", {
                                staticClass: "space",
                                on: {
                                  mousedown: function (t) {
                                    return e.$emit("linkPre", t, e.i, i);
                                  },
                                },
                              }),
                            ],
                          );
                        }),
                        0,
                      ),
                    ]),
                  ],
                ),
              ]);
        },
        de = [],
        he = {
          props: {
            item: { type: Object, default: () => {} },
            choice: { type: Object, default: () => {} },
            currentEvent: { type: String, default: () => "" },
            i: { type: Number, default: () => 0 },
          },
          data() {
            return {};
          },
          methods: {
            test() {},
            isVertical() {
              let e = { isVertical: !0 },
                t = localStorage.getItem("GlobalConfig");
              return (
                t && t.length > 0 && (e = Object.assign(e, JSON.parse(t))),
                e.isVertical
              );
            },
          },
        },
        pe = he,
        ge = (0, O.A)(pe, ue, de, !1, null, "16cfc268", null),
        me = ge.exports,
        _e = {
          name: "DAGBoard",
          props: {
            DataAll: { type: Object, default: () => [] },
            changeSizeNumber: Number,
            alimentCenterData: Boolean,
          },
          computed: {
            svgScale() {
              return this.svg_scale || sessionStorage["svgScale"]
                ? sessionStorage["svgScale"]
                : 1;
            },
          },
          created() {
            this.$nextTick(() => {
              this.setMouseWheelEvent();
            });
          },
          mounted() {
            ((sessionStorage["svg_left"] = 0), (sessionStorage["svg_top"] = 0));
          },
          methods: {
            startActive() {
              let e = this.step;
              if (
                e === this.historyList.length ||
                e > this.historyList.length ||
                !this.modelRunningStatus
              )
                return !1;
              (this.activeGraph(e),
                this.nextStep && clearTimeout(this.nextStep),
                (this.nextStep = setTimeout(
                  () => {
                    (this.step++, this.startActive());
                  },
                  1e3 *
                    (this.historyList[e + 1].time - this.historyList[e].time),
                )));
            },
            atMouseOut() {
              this.currentEvent = null;
            },
            dragPre(e, t, s) {
              ((this.multipleSelectNodes = JSON.parse(
                JSON.stringify(this.choice),
              )),
                this.multipleSelectNodes &&
                  this.multipleSelectNodes.paneNode.length &&
                  (this.initMultiplePosition = JSON.parse(
                    JSON.stringify(this.DataAll.nodes),
                  )),
                this.setInitRect(),
                (this.currentEvent = "dragPane"),
                (sessionStorage["offsetX"] = e.offsetX),
                (sessionStorage["offsetY"] = e.offsetY),
                (this.choice.index = t),
                (this.timeStamp = e.timeStamp),
                this.selPaneNode(s.id),
                this.setDragFramePosition(e),
                e.preventDefault(),
                e.stopPropagation(),
                (e.cancelBubble = !0));
            },
            dragIng(e) {
              switch (this.currentEvent) {
                case "dragPane":
                  this.paneDragIng(e);
                  break;
                case "dragLink":
                  this.setDragLinkPostion(e);
                  break;
                case "sel_area_ing":
                  this.setSelAreaPostion(e);
                  break;
                case "move_graph":
                  this.graphMoveIng(e);
                  break;
                default:
              }
            },
            dragEnd(e) {
              switch (this.currentEvent) {
                case "sel_area_ing":
                  this.getSelNodes(this.simulate_sel_area);
                  break;
                default:
              }
              this.currentEvent = null;
            },
            svgMouseDown(e) {
              (this.setInitRect(),
                "sel_area" === this.currentEvent
                  ? this.selAreaStart(e)
                  : ((this.currentEvent = "move_graph"), this.graphMovePre(e)));
            },
            linkPre(e, t, s) {
              (this.randomid(),
                this.setInitRect(),
                (this.currentEvent = "dragLink"),
                (this.choice = Object.assign({}, this.choice, {
                  index: t,
                  point: s,
                })),
                this.setDragLinkPostion(e, !0),
                e.preventDefault(),
                e.stopPropagation());
            },
            linkEnd(e, t) {
              if ("dragLink" === this.currentEvent) {
                let s = {
                    desp: {
                      src_node_id: this.DataAll.nodes[this.choice.index].id,
                      src_output_idx: this.choice.point,
                      dst_node_id: this.DataAll.nodes[e].id,
                      dst_input_idx: t,
                    },
                  },
                  i = {
                    set: this.DataAll.nodes[this.choice.index].pipelineIndex,
                    get: this.DataAll.nodes[e].pipelineIndex,
                    id: this.DataAll.nodes[e].id,
                  };
                const a = this;
                this.addEdge(s, a, i);
              }
              this.currentEvent = null;
            },
            sizeInit() {
              (this.changeSizeMethods("init"),
                (this.svg_left = 0),
                (this.svg_top = 0),
                (sessionStorage["svg_left"] = 0),
                (sessionStorage["svg_top"] = 0));
            },
            sizeExpend() {
              this.changeSizeMethods("expend");
            },
            sizeShrink() {
              this.changeSizeMethods("shrink");
            },
            onMouseWheel(e) {
              if (!e) return !1;
              let t = e.wheelDelta / 10;
              this.canMouseWheelUse &&
                t * t > 1 &&
                (t > 0 ? this.sizeExpend() : this.sizeShrink(),
                (this.canMouseWheelUse = !1),
                setTimeout(() => {
                  this.canMouseWheelUse = !0;
                }, 50));
            },
            setMouseWheelEvent() {
              const e = (e, t, s) => {
                e.attachEvent
                  ? e.attachEvent("on" + t, s)
                  : e.addEventListener(t, s, !1);
              };
              var t = document.getElementById("svgContent");
              (e(t, "mousewheel", this.onMouseWheel),
                e(t, "DOMMouseScroll", this.onMouseWheel));
            },
            sel_area() {
              ((this.currentEvent = "sel_area"),
                (this.simulate_sel_area = {
                  left: 0,
                  top: 0,
                  width: 0,
                  height: 0,
                }));
            },
            paneDragIng(e) {
              let t = sessionStorage["offsetX"] || 0,
                s = sessionStorage["offsetY"] || 0;
              const i =
                  (e.x -
                    this.initPos.left -
                    (sessionStorage["svg_left"] || 0)) /
                    this.svgScale -
                  30 -
                  t,
                a =
                  (e.y - this.initPos.top - (sessionStorage["svg_top"] || 0)) /
                    this.svgScale -
                  s;
              let n = {
                model_id: sessionStorage["newGraph"],
                id: this.DataAll.nodes[this.choice.index].id,
                pos_x: i,
                pos_y: a,
              };
              this.multipleMoveNode &&
              this.multipleSelectNodes.paneNode.length > 1
                ? this.multipleMoveNode(n)
                : this.moveNode(n);
            },
            paneDragEnd(e) {
              ((this.multipleSelectNodes = {}),
                (this.initMultiplePosition = null),
                (this.dragFrame = { dragFrame: !1, posX: 0, posY: 0 }));
              const t =
                  (e.x -
                    this.initPos.left -
                    (sessionStorage["svg_left"] || 0)) /
                    this.svgScale -
                  90,
                s =
                  (e.y - this.initPos.top - (sessionStorage["svg_top"] || 0)) /
                    this.svgScale -
                  15;
              (sessionStorage["newGraph"],
                this.DataAll.nodes[this.choice.index].id);
            },
            selPaneNode(e) {
              ((this.choice.paneNode.length = []),
                e &&
                  (this.choice.paneNode.push(e),
                  this.$emit("updateDAG", this.DataAll, "selectNode", e)));
            },
            selAreaStart(e) {
              this.currentEvent = "sel_area_ing";
              const t =
                  (e.x -
                    this.initPos.left -
                    (sessionStorage["svg_left"] || 0)) /
                  this.svgScale,
                s =
                  (e.y - this.initPos.top - (sessionStorage["svg_top"] || 0)) /
                  this.svgScale;
              this.simulate_sel_area = { left: t, top: s, width: 0, height: 0 };
            },
            setSelAreaPostion(e) {
              const t =
                  (e.x -
                    this.initPos.left -
                    (sessionStorage["svg_left"] || 0)) /
                  this.svgScale,
                s =
                  (e.y - this.initPos.top - (sessionStorage["svg_top"] || 0)) /
                  this.svgScale,
                i = t - this.simulate_sel_area.left,
                a = s - this.simulate_sel_area.top;
              ((this.simulate_sel_area.width = i),
                (this.simulate_sel_area.height = a));
            },
            getSelNodes(e) {
              const { left: t, top: s, width: i, height: a } = e;
              ((this.choice.paneNode.length = 0),
                this.DataAll.nodes.forEach((e) => {
                  e.pos_x > t &&
                    e.pos_x < t + i &&
                    e.pos_y > s &&
                    e.pos_y < s + a &&
                    this.choice.paneNode.push(e.id);
                }),
                (this.simulate_sel_area = {
                  left: 0,
                  top: 0,
                  width: 0,
                  height: 0,
                }));
            },
            focusInput(e) {
              e && e.focus();
            },
            graphMovePre(e) {
              const { x: t, y: s } = e;
              ((this.svg_trans_init = { x: t, y: s }),
                (this.svg_trans_pre = { x: this.svg_left, y: this.svg_top }));
            },
            graphMoveIng(e) {
              const { x: t, y: s } = this.svg_trans_init;
              ((this.svg_left = e.x - t + this.svg_trans_pre.x),
                (this.svg_top = e.y - s + this.svg_trans_pre.y),
                (sessionStorage["svg_left"] = this.svg_left),
                (sessionStorage["svg_top"] = this.svg_top));
            },
            setDragFramePosition(e) {
              const t =
                  e.x - this.initPos.left - (sessionStorage["svg_left"] || 0),
                s = e.y - this.initPos.top - (sessionStorage["svg_top"] || 0);
              this.dragFrame = {
                posX: t / this.svgScale - 90,
                posY: s / this.svgScale - 15,
              };
            },
            setDragLinkPostion(e, t) {
              const s =
                  (e.x -
                    this.initPos.left -
                    (sessionStorage["svg_left"] || 0)) /
                  this.svgScale,
                i =
                  (e.y - this.initPos.top - (sessionStorage["svg_top"] || 0)) /
                  this.svgScale;
              (t &&
                (this.dragLink = Object.assign({}, this.dragLink, {
                  fromX: s,
                  fromY: i,
                })),
                (this.dragLink = Object.assign({}, this.dragLink, {
                  toX: s,
                  toY: i,
                })));
            },
            close_click_nodes() {
              this.is_edit_area = { value: !1, x: -9999, y: -9999 };
            },
            r_click_nodes(e, t) {
              this.setInitRect();
              const s = this.DataAll.nodes[t].id,
                i = this.DataAll.nodes[t].detail || null,
                a = this.DataAll.nodes[t].rightClickEvent || null,
                n = e.x - this.initPos.left,
                l = e.y - this.initPos.top;
              return (
                (this.is_edit_area = {
                  value: !0,
                  x: n,
                  y: l,
                  id: s,
                  detail: i,
                  rightClickEvent: a,
                }),
                e.stopPropagation(),
                (e.cancelBubble = !0),
                e.preventDefault(),
                !1
              );
            },
            setInitRect() {
              let { left: e, top: t } = document
                .getElementById("svgContent")
                .getBoundingClientRect();
              this.initPos = { left: e, top: t };
            },
            changeModelRunningStatus(e) {
              this.$emit("updateDAG", this.DataAll, "startRunning");
            },
            activeGraph: ({ commit: e, state: t }, s) => {},
            stopGraph: ({ commit: e, state: t }) => {},
            addEdge: (e, t, s) => {
              let i = t.DataAll;
              const { set: a, get: n } = s;
              if (a == n) return t.$message.error("不能自己连接自己");
              const l = i.nodes.find((e) => e.pipelineIndex == a)?.connection
                ?.followers;
              l.includes(n)
                ? ((i.edges = i.edges || []),
                  i.edges.push({ ...e.desp, id: t.randmid }))
                : t.$message.error("属性不符，不允许连接");
            },
            delEdge({ id: e }) {
              if (this.DataAll.edges) {
                const t = this.DataAll.edges.findIndex((t) => t.id == e);
                this.DataAll.edges.splice(t, 1);
              }
              this.$emit("updateDAG", this.DataAll, "delEdge");
            },
            moveNode(e) {
              const { id: t, pos_x: s, pos_y: i } = e;
              let a = this.DataAll;
              (a.nodes.forEach((t, s) => {
                t.id === e.id && ((t.pos_x = e.pos_x), (t.pos_y = e.pos_y));
              }),
                this.$emit("updateDAG", a, "moveNode"));
            },
            multipleMoveNode(e) {
              const { id: t, pos_x: s, pos_y: i } = e;
              let a = 0,
                n = 0,
                l = this.initMultiplePosition,
                o = this.DataAll;
              (l.map((e) => {
                e.id === t && ((a = s - e.pos_x), (n = i - e.pos_y));
              }),
                l.forEach((e) => {
                  this.multipleSelectNodes.paneNode.indexOf(e.id) > -1 &&
                    ((e.pos_x += a), (e.pos_y += n));
                }),
                (o.nodes = l),
                this.$emit("updateDAG", o, "moveNode"));
            },
            addNode: (e) => {
              let t = (void 0).DataAll.nodes;
              (t.push({
                ...e.desp,
                id: taht.randmid,
                in_ports: [0],
                out_ports: [0],
              }),
                (void 0).$emit("updateDag", (void 0).DataAll, "addNode"));
            },
            delNode({ model_id: e, id: t }) {
              let s = [],
                i = [];
              (this.DataAll.edges &&
                this.DataAll.edges.forEach((e) => {
                  e.dst_node_id !== t && e.src_node_id !== t && s.push(e);
                }),
                this.DataAll.nodes.forEach((e) => {
                  e.id !== t && i.push(e);
                }),
                (this.DataAll.edges = s),
                (this.DataAll.nodes = i),
                this.$emit("updateDAG", this.DataAll, "delNode"));
            },
            changeSizeMethods(e) {
              let t =
                  "string" === typeof sessionStorage["svgScale"]
                    ? Number(sessionStorage["svgScale"])
                    : 1,
                s = window.innerWidth,
                i = window.innerHeight;
              switch (e) {
                case "shrink":
                  ((t -= 0.05),
                    (this.svg_left = sessionStorage["svg_left"] =
                      this.svg_left + 0.01 * s),
                    (this.svg_top = sessionStorage["svg_top"] =
                      this.svg_top + 0.01 * i));
                  break;
                case "expend":
                  ((t += 0.05),
                    (this.svg_top = sessionStorage["svg_top"] =
                      this.svg_top - 0.01 * i),
                    (this.svg_left = sessionStorage["svg_left"] =
                      this.svg_left - 0.01 * s));
                  break;
                case "init":
                  t = 1;
                  break;
                default:
              }
              this.svg_scale = sessionStorage["svgScale"] = t;
            },
            changeNodeName(e) {
              (this.DataAll.nodes.forEach((t) => {
                t.id === e.id && (t.name = e.name);
              }),
                this.$emit("updateDAG", this.DataAll, "changeNodeName"));
            },
            changePort(e, t) {
              (this.DataAll.nodes.forEach((s) => {
                s.id === t && (s[e] ? s[e].push(s[e].length) : (s[e] = ["0"]));
              }),
                this.$emit("updateDAG", this.DataAll, "changePort"));
            },
            editNodeDetails(e) {
              this.$emit("editNodeDetails", e);
            },
            nodesPersonalEvent(e, t) {
              this.$emit("doSthPersonal", e, t);
            },
            randomid() {
              for (var e = this.DataAll.nodes, t = [], s = 0; s < e.length; s++)
                t.push(e[s].id);
              for (
                var i = Math.floor(999999 * Math.random()) + 1, a = 0;
                a < t.length;
                a++
              )
                if (i == t[a]) {
                  (console.log("有重复的重新随机"), this.randomid());
                  break;
                }
              this.randmid = i;
            },
          },
          watch: {
            changeSizeNumber: {
              handler(e) {
                this.changeSizeMethods(
                  e > 0 ? "expend" : e < 0 ? "shrink" : "init",
                );
              },
            },
            alimentCenterData() {
              ((this.svg_left = 0),
                (this.svg_top = 0),
                (sessionStorage["svg_left"] = this.svg_left),
                (sessionStorage["svg_top"] = this.svg_top));
            },
          },
          data() {
            return {
              randmid: "",
              svg_scale: null,
              choice: { paneNode: [], index: -1, point: -1 },
              dragFrame: { posX: 9999, posY: 9999 },
              dragLink: { fromX: 0, fromY: 0, toX: 0, toY: 0 },
              currentEvent: null,
              initPos: { left: -1, top: -1 },
              timeStamp: "",
              is_edit_area: { value: !1, x: -9999, y: -9999 },
              simulate_sel_area: { left: 10, top: 50, width: 0, height: 0 },
              svg_left: 0,
              svg_top: 0,
              svg_trans_init: { x: 0, y: 0 },
              canMouseWheelUse: !0,
              step: 0,
              modelRunningStatus: !1,
              nextStep: null,
              multipleSelectNodes: {},
              initMultiplePosition: {},
            };
          },
          components: {
            Arrow: z,
            SimulateArrow: T,
            SimulateFrame: X,
            EditArea: Q,
            Control: ie,
            SimulateSelArea: ce,
            mainBody: me,
          },
        },
        ve = _e,
        fe = (0, O.A)(ve, C, $, !1, null, "242c9fd1", null),
        ye = fe.exports,
        xe = function () {
          var e = this,
            t = e._self._c;
          return t(
            "div",
            {
              staticClass: "nodesBus-contain",
              style: {
                left: this.pos_x + 90 + "px",
                top: this.pos_y - 110 + "px",
              },
            },
            [
              t("div", { staticClass: "nodesBus" }, [
                t("span", { staticClass: "icon" }),
                t("span", { staticClass: "name" }, [e._v(e._s(e.value))]),
              ]),
            ],
          );
        },
        Se = [],
        be = {
          name: "NodeBus",
          props: {
            value: { type: String, default: "传入内容" },
            pos_x: { type: Number },
            pos_y: { type: Number },
          },
          data() {
            return { name: this.value, left: this.pos_x, top: this.pos_y };
          },
        },
        ke = be,
        we = (0, O.A)(ke, xe, Se, !1, null, "61d1c0ad", null),
        Ce = we.exports,
        $e = {
          name: "ProjectDetail",
          components: { DAGBoard: ye, NodeBus: Ce },
          data() {
            return {
              alimentCenterData: !0,
              openDir: "",
              createCodeToLocal: "",
              downs: n,
              folter: l,
              file: o,
              collect: u,
              collectActive: d,
              empty: r,
              iconImg: h,
              changesImg: l,
              save: p,
              chexiao: g,
              huifu: m,
              yunxing: _,
              enlarge: v,
              enlargeJian: f,
              huanyuan: y,
              jizhong: x,
              quanping: S,
              shouqi: b,
              xiangyou: k,
              createCode: c,
              changeSizeNumber: 0,
              tabList: [
                { id: 1, name: "项目" },
                { id: 2, name: "导出" },
                { id: 3, name: "历史任务" },
                { id: 4, name: "生成模型" },
              ],
              currentIndex: -1,
              activeName: "",
              initNodesBasic: w.xn,
              yourJSONDataFillThere: { nodes: [], sides: [] },
              dragBus: !1,
              busValue: { value: "name", pos_x: 100, pos_y: 100 },
              formRowList: [],
              resourceIsShow: !1,
            };
          },
          created() {
            (console.log(w.xn),
              w.xn.forEach((e) => {
                "Module" === e.type &&
                  e.spec.forEach((e) => {
                    "Module" === e.type
                      ? e.spec.forEach((e) => {
                          "Object" === e.type && this.handleData(e);
                        })
                      : "Object" === e.type && this.handleData(e);
                  });
              }));
          },
          watch: {
            openDir(e) {
              switch (e) {
                case "0":
                  this.openDirectory();
                  break;
                case "1":
                  break;
              }
            },
            createCodeToLocal(e) {
              switch (e) {
                case "0":
                  this.goRun(0);
                  break;
                case "1":
                  this.handleSave();
                  break;
                case "2":
                  this.goRun(1);
                  break;
                case "3":
                  break;
              }
            },
          },
          mounted() {
            (this.drageDomChangeSize(),
              this.drageDomChnageSizeLeft(),
              this.echoData());
          },
          computed: {
            visualProgramRow() {
              return JSON.parse(this.$route.query.row);
            },
          },
          methods: {
            alimentCenter() {
              this.alimentCenterData = !this.alimentCenterData;
            },
            drageDomChangeSize() {
              const e = this.$refs.pseudoDomRight,
                t = document.documentElement.clientWidth,
                s = this.$refs.fixedRight;
              (console.log(s),
                (e.onmousedown = (i) => {
                  ((document.onmousemove = (i) => {
                    (console.log(t - i.screenX),
                      (e.parentNode.style.width = t - i.screenX + "px"),
                      (s.style.right = t - i.screenX + 18 + "px"));
                  }),
                    (document.onmouseup = (e) => {
                      ((document.onmousemove = null),
                        (document.onmouseup = null));
                    }));
                }),
                (document.onmouseup = (e) => {
                  ((document.onmousemove = null), (document.onmouseup = null));
                }));
            },
            drageDomChnageSizeLeft() {
              const e = this.$refs.pseudoDomLeft;
              ((e.onmousedown = (t) => {
                ((document.onmousemove = (t) => {
                  e.parentNode.style.width = t.screenX + "px";
                }),
                  (document.onmouseup = (e) => {
                    ((document.onmousemove = null),
                      (document.onmouseup = null));
                  }));
              }),
                (document.onmouseup = (e) => {
                  ((document.onmousemove = null), (document.onmouseup = null));
                }));
            },
            handleData(e) {
              e.parameter.forEach((e) => {
                (Array.isArray(e.input_array) &&
                  e.input_array.length > 1 &&
                  (e.selfChoice = e.input_array[0].input_type),
                  Array.isArray(e.input_array) &&
                    e.input_array.forEach((e) => {
                      switch (e.input_type) {
                        case "user_filepath":
                          e.result3 =
                            -1 !== e.default.indexOf(":")
                              ? e.default.split(":")[1]
                              : "";
                          break;
                        case "single_choice":
                          e.default0 =
                            -1 !== e.default.indexOf(":")
                              ? e.default.substring(e.default.indexOf(":") + 1)
                              : "";
                          break;
                        case "single_choice_object":
                          e.default0 =
                            -1 !== e.default.indexOf(":")
                              ? e.default.split(":")[1]
                              : "";
                          break;
                        case "boolean":
                          e.default0 =
                            -1 !== e.default.indexOf(":")
                              ? e.default.split(":")[1]
                              : "";
                          break;
                        case "multiple_choice":
                          e.conditions =
                            -1 !== e.default.indexOf(":")
                              ? [e.default.split(":")[1]]
                              : [];
                          break;
                        case "int":
                          e.result =
                            -1 !== e.default.indexOf(":")
                              ? e.default.split(":")[1]
                              : void 0;
                          break;
                        case "float":
                          e.result2 =
                            -1 !== e.default.indexOf(":")
                              ? e.default.split(":")[1]
                              : void 0;
                          break;
                        case "str":
                          e.result4 =
                            -1 !== e.default.indexOf(":")
                              ? e.default.split(":")[1]
                              : "";
                          break;
                        case "url":
                          e.result5 =
                            -1 !== e.default.indexOf(":")
                              ? e.default.split(":")[1]
                              : "";
                          break;
                        case "list":
                          e.result6 =
                            -1 !== e.default.indexOf(":")
                              ? e.default.split(":")[1]
                              : "";
                          break;
                        case "tuple":
                          e.result7 =
                            -1 !== e.default.indexOf(":")
                              ? e.default.split(":")[1]
                              : "";
                          break;
                      }
                    }));
              });
            },
            async echoData() {
              try {
                const e = await this.$axios({
                  url: "/api/longriver/graph/get",
                  method: "post",
                  data: { project_id: this.visualProgramRow.id, user_id: 1 },
                });
                this.yourJSONDataFillThere = (e.data.data[0] &&
                  e.data.data[0][3] &&
                  JSON.parse(e.data.data[0][3])) || {
                  edges: [],
                  nodes: [],
                  sides: [],
                };
              } catch (e) {}
            },
            handleTab(e) {
              this.currentIndex = e;
            },
            handleCommand(e) {
              switch (e) {
                case "a":
                  console.log("查看项目信息");
                  break;
                case "b":
                  console.log("修改项目信息");
                  break;
                case "c":
                  console.log("代码");
                  break;
                case "d":
                  console.log("图片");
                  break;
                case "e":
                  console.log("源文件");
                  break;
              }
            },
            goBack() {
              this.$router.replace("/visualProgram");
            },
            sizeChange(e) {
              switch (e) {
                case "+":
                  (console.log("放大"),
                    this.changeSizeNumber > 0
                      ? this.changeSizeNumber++
                      : (this.changeSizeNumber = 1));
                  break;
                case "-":
                  (console.log("缩小"),
                    this.changeSizeNumber < 0
                      ? this.changeSizeNumber--
                      : (this.changeSizeNumber = -1));
                  break;
                case "init":
                  (console.log("恢复"), (this.changeSizeNumber = 0));
                  break;
                case "fullScreen":
                  (console.log("全屏"), this.fullScreenMethod());
                  break;
                case "exitFullScreen":
                  (console.log("退出全屏"), this.exitFullScreenMethod());
                  break;
              }
            },
            fullScreenMethod() {
              const e = document.querySelector("#visualDetailsMain");
              e.requestFullscreen
                ? e.requestFullscreen()
                : e.webkitRequestFullScreen
                  ? e.webkitRequestFullScreen()
                  : e.mozRequestFullScreen
                    ? e.mozRequestFullScreen()
                    : e.msRequestFullscreen && e.msRequestFullscreen();
            },
            exitFullScreenMethod() {
              document.exitFullscreen
                ? document.exitFullscreen()
                : document.webkitCancelFullScreen
                  ? document.webkitCancelFullScreen()
                  : document.mozCancelFullScreen
                    ? document.mozCancelFullScreen()
                    : document.msExitFullscreen && document.msExitFullscreen();
            },
            async openDirectory() {
              const { id: e } = this.visualProgramRow,
                t = { user_id: 1, project_id: e };
              try {
                const e = await this.$axios.post(
                  "/api/longriver/files/open-window",
                  t,
                );
                this.$message.success(e.data.status);
              } catch (s) {
                this.$message.error("系统异常");
              }
            },
            async handleSave() {
              const { nodes: e, edges: t } = this.yourJSONDataFillThere;
              if (!e || !e.length)
                return this.$message.error("请至少生成一个节点再保存");
              try {
                const { id: e } = this.visualProgramRow,
                  t = await this.$axios.post("/api/longriver/graph/save/", {
                    project_id: e,
                    user_id: 1,
                    graph: JSON.stringify(this.yourJSONDataFillThere),
                    project_type: 4,
                  });
                "保存成功" === t.data.status
                  ? this.$message.success("保存成功")
                  : this.$message.success(t.data.status);
              } catch (s) {
                this.$message.error("系统异常");
              }
            },
            goRun(e) {
              const { nodes: t, edges: s } = this.yourJSONDataFillThere;
              if (6 !== t.length)
                return this.$message.error(
                  "目前模型不能生成代码，请检查没有添加的模型",
                );
              if (5 !== s.length)
                return this.$message.error("请检查是否所有的节点都连上线了");
              const i = JSON.parse(JSON.stringify(t));
              const hasValue = (v) => v !== undefined && v !== null && v !== "";
              const toRaw = (v, inputType) => inputType + ":" + (hasValue(v) ? v : "");
              const toChoice = (v, inputType) =>
                v === "None" ? "object:None" : inputType + ":" + (hasValue(v) ? v : "");
              i.forEach((e) => {
                ((e.connection.followers = []), (e.connection.following = []));
                let t = [],
                  a = [];
                (s.forEach((s) => {
                  if (e.id == s.src_node_id) {
                    let a = i.filter((e) => e.id == s.dst_node_id) || [];
                    (t.push(...a),
                      (e.connection.followers = t.map((e) => e.pipelineIndex)));
                  }
                  if (e.id == s.dst_node_id) {
                    let t = i.filter((e) => e.id == s.src_node_id) || [];
                    (a.push(...t),
                      (e.connection.following = a.map((e) => e.pipelineIndex)));
                  }
                }),
                  1 == e.pipelineIndex &&
                    (e.connection.following = ["starting_node"]),
                  6 == e.pipelineIndex &&
                    (e.connection.followers = ["end_node"]));
              });
              let a = [];
              i.forEach((e) => {
                const filteredParams = (e.params || []).filter(
                  (p) => p.internal_name !== "min_impurity_split"
                );
              
                a.push({
                  internal_name: e.internal_name,
                  connection: { ...e.connection, id: e.connection.index },
                  parameter: filteredParams,
                });
              
                filteredParams.forEach((e) => {
                  e.input_array &&
                    e.input_array.forEach((e) => {
                      switch (e.input_type) {
                        case "user_filepath":
                          e.values = toRaw(e.result3, e.input_type);
                          break;
                        case "single_choice":
                          e.values = toChoice(e.default0, e.input_type);
                          break;
                        case "single_choice_object":
                          e.values = toChoice(e.default0, e.input_type);
                          break;
                        case "boolean":
                          e.values = toRaw(e.default0, e.input_type);
                          break;
                        case "int":
                          e.values = toRaw(e.result, e.input_type);
                          break;
                        case "float":
                          e.values = toRaw(e.result2, e.input_type);
                          break;
                        case "str":
                          e.values = toRaw(e.result4, e.input_type);
                          break;
                        case "url":
                          e.values = toRaw(e.result5, e.input_type);
                          break;
                        case "list":
                          e.values = toRaw(e.result6, e.inputType || e.input_type);
                          break;
                        case "tuple":
                          e.values = toRaw(e.result7, e.input_type);
                          break;
                        case "None":
                          e.values = "object:None";
                          break;
                      }
                    });
                  
                  delete e.description;
                  delete e.external_name;
                  delete e.type;
                });
              });
              const n = JSON.parse(JSON.stringify(a));
              for (let o = 0; o < n.length; o++) {
                const e = n[o];
                for (let t = 0; t < e.parameter.length; t++) {
                  const s = e.parameter[t];
                  if (s.input_array.length > 1) {
                    const e = s.input_array.find(
                      (e) => e.input_type == s.selfChoice,
                    );
                    if (!e) return this.$message.error("请填写完整");
                    if (!e.values.split(":")[1])
                      return this.$message.error("请填写完整");
                    ((s.values = e.values),
                      delete s.input_array,
                      delete s.selfChoice);
                  } else {
                    const e = s.input_array[0].values;
                    if (-1 !== e.indexOf(":") && !e.split(":")[1])
                      return this.$message.error("请填写完整");
                    ((s.values = s.input_array[0].values),
                      delete s.input_array);
                  }
                }
              }
              n.unshift({
                internal_name: "metadata",
                connection: {
                  index: "-1",
                  id: "-1",
                  following: ["no_node"],
                  followers: ["no_node"],
                },
                bl_run_generate_code: e,
              });
              const l = {
                countJson: n,
                project_id: this.visualProgramRow.id,
                project_type: this.visualProgramRow.type,
                graph: JSON.stringify(this.yourJSONDataFillThere),
              };
              this.$axios
                .post("/api/longriver/pyml", l)
                .then((e) => {
                  "multiprocessing ok" === e.data.status
                    ? this.$message.success("运行成功")
                    : this.$message.success(e.data.status);
                })
                .catch(() => {
                  this.$message.error("系统异常");
                });
            },
            integerBlur(e, t) {
              (console.log(t),
                t.conditions.includes("positive-integer") &&
                  e.target.value <= 0 &&
                  ((e.target.value = null),
                  (t.result = null),
                  this.$message.error("只能输入正整数")),
                t.conditions.includes("negative-integer") &&
                  e.target.value >= 0 &&
                  ((e.target.value = null),
                  (t.result = null),
                  this.$message.error("只能输入负整数")),
                t.conditions.includes("non-positive-integer") &&
                  e.target.value > 0 &&
                  ((e.target.value = null),
                  (t.result = null),
                  this.$message.error("只能输入非正整数")),
                t.conditions.includes("non-negative-integer") &&
                  e.target.value < 0 &&
                  ((e.target.value = null),
                  (t.result = null),
                  this.$message.error("只能输入非负整数")),
                t.conditions.includes("negative") &&
                  e.target.value >= 0 &&
                  ((e.target.value = null),
                  (t.result = null),
                  this.$message.error("只能输入负数")),
                t.conditions.includes("positive") &&
                  e.target.value <= 0 &&
                  ((e.target.value = null),
                  (t.result = null),
                  this.$message.error("只能输入正数")));
            },
            floatBlur(e, t) {
              (console.log(t),
                t.conditions.includes("percentage") &&
                  (e.target.value >= 1 || e.target.value <= 0) &&
                  ((e.target.value = null),
                  (t.result2 = null),
                  this.$message.error("只能输入0 ~ 1之间的值")),
                t.conditions.includes("positive-float") &&
                  e.target.value <= 0 &&
                  ((e.target.value = null),
                  (t.result2 = null),
                  this.$message.error("只能输入正浮点数")),
                t.conditions.includes("negative-float") &&
                  e.target.value >= 0 &&
                  ((e.target.value = null),
                  (t.result2 = null),
                  this.$message.error("只能输入负浮点数")),
                t.conditions.includes("non-positive-float") &&
                  e.target.value > 0 &&
                  ((e.target.value = null),
                  (t.result2 = null),
                  this.$message.error("只能输入非正浮点数")),
                t.conditions.includes("non-negative-float") &&
                  e.target.value < 0 &&
                  ((e.target.value = null),
                  (t.result2 = null),
                  this.$message.error("只能输入非负浮点数")),
                t.conditions.includes("non-negative") &&
                  e.target.value < 0 &&
                  ((e.target.value = null),
                  (t.result2 = null),
                  this.$message.error("只能输入非负数")),
                t.conditions.includes("non-positive") &&
                  e.target.value > 0 &&
                  ((e.target.value = null),
                  (t.result2 = null),
                  this.$message.error("只能输入非正数")),
                t.conditions.includes("over-half-percentage") &&
                  (e.target.value <= 0.5 || e.target.value >= 1) &&
                  ((e.target.value = null),
                  (t.result2 = null),
                  this.$message.error("只能输入0.5 ~ 1 之间的数")),
                t.conditions.includes("negative") &&
                  e.target.value >= 0 &&
                  ((e.target.value = null),
                  (t.result2 = null),
                  this.$message.error("只能输入负数")),
                t.conditions.includes("positive") &&
                  e.target.value <= 0 &&
                  ((e.target.value = null),
                  (t.result2 = null),
                  this.$message.error("只能输入正数")));
            },
            stringArrBlur(e, t) {
              const v = (e.target.value || "").trim();
              if (!v) {
                e.target.value = "";
                t.result6 = "";
                this.$message.error("请输入列表，比如['1', '2']");
                return;
              }
              try {
                const parsed = JSON.parse(v.replace(/'/g, '"'));
                if (!Array.isArray(parsed)) throw new Error("not array");
                t.result6 = v;
              } catch (err) {
                e.target.value = "";
                t.result6 = "";
                this.$message.error("请输入列表，比如['1', '2']");
              }
            },
            yuanBlur(e) {
              const t = e.target.value;
              if (0 == t)
                return (
                  (e.target.value = ""),
                  this.$message.error("请输入两个整数元组，比如(3,2)")
                );
              {
                let s = /^(0|[1-9]\d*)$/,
                  i = t,
                  a = t.length;
                if ("(" != i[0] || ")" != i[a - 1] || -1 == t.indexOf(","))
                  return (
                    (e.target.value = ""),
                    this.$message.error("请输入两个整数元组，比如(3,2)")
                  );
                {
                  let i = t.slice(1, t.indexOf(","));
                  if (!s.test(i)) {
                    let t = /^-[1-9]\d*$/;
                    return (
                      t.test(i),
                      (e.target.value = ""),
                      this.$message.error("请输入两个整数元组，比如(3,2)")
                    );
                  }
                  let a = t.slice(t.indexOf(",") + 1, t.length - 1);
                  if (s.test(a));
                  else {
                    let t = /^-[1-9]\d*$/;
                    if (!t.test(a))
                      return (
                        (e.target.value = ""),
                        this.$message.error("请输入两个整数元组，比如(3,2)")
                      );
                  }
                }
              }
            },
            monitor() {
              ((this.resourceIsShow = !0),
                this.$nextTick(() => {
                  this.initEcharts();
                }));
            },
            goDetail() {
              console.log("跳转到项目详情");
            },
            packUp() {
              this.resourceIsShow = !1;
            },
            handleCollect(e, t) {
              (0 === t ? (e.isCollect = !0) : 1 === t && (e.isCollect = !1),
                this.$forceUpdate());
            },
            initEcharts() {
              const e = this.$echarts.init(
                  document.getElementById("content-cpu"),
                ),
                t = this.$echarts.init(document.getElementById("content-gpu")),
                s = this.$echarts.init(
                  document.getElementById("content-storage"),
                ),
                i = ["2018", "2019", "2020", "2021", "2022", "2023"];
              let a = [];
              a.push({
                name: "",
                type: "line",
                data: [33, 40, 43, 33, 42, 1],
                symbolSize: 2,
                symbol: "circle",
                lineStyle: { color: "#27BABE", width: 1 },
                itemStyle: {
                  color: "#27BABE",
                  borderColor: "#27BABE",
                  borderWidth: 5,
                },
                areaStyle: {
                  color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                    { offset: 0, color: "#C0EEEC" },
                    { offset: 1, color: "#E9EFF0" },
                  ]),
                },
                emphasis: { scale: 1.5 },
              });
              const n = {
                tooltip: {
                  trigger: "axis",
                  formatter: function (e) {
                    const { axisValue: t, value: s } = e[0];
                    return `\n                                <div>时间：${t}</div>\n                                <div>使用率：${s}%</div>\n                            `;
                  },
                },
                grid: {
                  left: "2%",
                  right: "6%",
                  top: "6%",
                  bottom: "4%",
                  containLabel: !0,
                },
                xAxis: {
                  type: "category",
                  data: i,
                  boundaryGap: !1,
                  axisTick: { show: !1 },
                  axisLine: { lineStyle: { color: "rgba(204, 204, 204, 1)" } },
                  axisLabel: {
                    show: !0,
                    textStyle: {
                      fontSize: 14,
                      color: "rgba(0, 0, 0, 0.65)",
                      fontFamily: "Source Han Sans CN-Regular",
                    },
                  },
                },
                yAxis: {
                  name: "",
                  nameTextStyle: {
                    fontSize: 14,
                    color: "rgba(0, 0, 0, 0.65)",
                    fontFamily: "Source Han Sans CN-Regular",
                    align: "left",
                    verticalAlign: "center",
                  },
                  type: "value",
                  axisTick: { show: !1 },
                  splitLine: {
                    lineStyle: {
                      type: "dashed",
                      width: 1,
                      color: "rgba(223, 223, 223, 1)",
                      opacity: "1",
                    },
                  },
                  axisLine: { show: !1 },
                  axisLabel: {
                    show: !0,
                    textStyle: {
                      fontSize: 14,
                      color: "rgba(0, 0, 0, 0.65)",
                      fontFamily: "HarmonyOS Sans-Regular",
                    },
                    formatter: "{value}%",
                  },
                  splitArea: { show: !1 },
                },
                series: a,
              };
              (e.setOption(n), t.setOption(n), s.setOption(n));
            },
            startNodesBus(e) {
              let t = null;
              if (
                (sessionStorage["dragDes"] &&
                  (t = JSON.parse(sessionStorage["dragDes"])),
                t && t.drag)
              ) {
                const s = e.pageX,
                  i = e.pageY + 70;
                ((this.busValue = Object.assign({}, this.busValue, {
                  pos_x: s,
                  pos_y: i,
                  value: t.fun,
                })),
                  (this.dragBus = !0));
              }
            },
            moveNodesBus(e) {
              if (this.dragBus) {
                const t = e.pageX,
                  s = e.pageY + 70;
                this.busValue = Object.assign({}, this.busValue, {
                  pos_x: t,
                  pos_y: s,
                });
              }
            },
            endNodesBus(e) {
              let t = null;
              sessionStorage["dragDes"] &&
                (t = JSON.parse(sessionStorage["dragDes"]));
              var s = navigator.userAgent,
                i = s.indexOf("Firefox") > -1;
              if (
                e.toElement &&
                t &&
                t.drag &&
                "svgContent" === e.toElement.id &&
                !i
              ) {
                const s =
                    (e.offsetX - 90 - (sessionStorage["svg_left"] || 0)) /
                    (sessionStorage["svgScale"] || 1),
                  i =
                    (e.offsetY - 15 - (sessionStorage["svg_top"] || 0)) /
                    (sessionStorage["svgScale"] || 1);
                delete t.drag;
                const a = {
                  model_id: sessionStorage["newGraph"],
                  desp: { pos_x: s, pos_y: i, name: this.busValue.value, ...t },
                };
                this.randomid();
                let n = JSON.parse(
                    JSON.stringify(this.yourJSONDataFillThere.nodes),
                  ),
                  l = {
                    ...a.desp,
                    id: this.randmid,
                    in_ports: [0],
                    out_ports: [0],
                  };
                if (n) {
                  const e = n.some((e) => e.pipelineIndex == l.pipelineIndex);
                  if (e)
                    ((window.sessionStorage["dragDes"] = null),
                      (this.dragBus = !1),
                      this.$message.error("已经有同属性"));
                  else {
                    this.yourJSONDataFillThere.nodes.push({ ...l });
                    const e = this.yourJSONDataFillThere.nodes.find((e) =>
                      e.connection?.followers.includes(l.pipelineIndex),
                    );
                    if (e) {
                      this.yourJSONDataFillThere.edges =
                        this.yourJSONDataFillThere.edges || [];
                      for (
                        let e = 0;
                        e < this.yourJSONDataFillThere.nodes.length;
                        e++
                      ) {
                        const t = this.yourJSONDataFillThere.nodes[e];
                        if (
                          t.connection?.followers.find(
                            (e) => e == l.pipelineIndex,
                          )
                        ) {
                          this.yourJSONDataFillThere.edges.push({
                            src_node_id: t?.id,
                            dst_node_id: l.id,
                            id: this.randmid,
                            src_output_idx: 0,
                            dst_input_idx: 0,
                          });
                          break;
                        }
                      }
                    }
                  }
                }
              }
              ((window.sessionStorage["dragDes"] = null), (this.dragBus = !1));
            },
            updateDAG(e, t, s) {
              switch (t) {
                case "selectNode":
                  this.showNodeDetails(e.nodes.find((e) => e.id === s));
                  break;
                case "delEdge":
                  setTimeout(() => {
                    this.yourJSONDataFillThere.edges = e.edges;
                  }, 100);
                  break;
                default:
              }
            },
            editNodeDetails() {
              console.log(...arguments);
            },
            doSthPersonal() {
              console.log(...arguments);
            },
            dragIt(e) {
              const {
                  type: t,
                  external_name: s,
                  description: i,
                  internal_name: a,
                  parameter: n,
                  connection: l,
                } = e,
                o = {
                  internal_name: a,
                  description: i,
                  fun: s,
                  name: s,
                  pipelineIndex: l.index,
                  connection: l,
                  setparams: {},
                  type: t,
                  params: n,
                };
              sessionStorage["dragDes"] = JSON.stringify({ drag: !0, ...o });
            },
            randomid() {
              let e = this.yourJSONDataFillThere.nodes,
                t = [];
              for (var s = 0; s < e.length; s++) t.push(e[s].id);
              for (
                var i = Math.floor(99999 * Math.random()) + 1, a = 0;
                a < t.length;
                a++
              )
                if (i == t[a]) {
                  this.randomid();
                  break;
                }
              this.randmid = i;
            },
            showNodeDetails(e) {
              this.formRowList = e?.params;
            },
          },
        },
        De = $e,
        Ne = (0, O.A)(De, i, a, !1, null, "c2f5ddb2", null),
        Ae = Ne.exports;
    },
  },
]);
